# backend/main.py
import json
from dataclasses import asdict
from typing import List, Optional, Tuple
import re

import networkx as nx
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Import graph loader
from graph_loader import get_graph, set_active_graph, get_active_graph_name, list_available_graphs, get_graph_info

app = FastAPI()

# Allow local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------- Trace event ---------
from dataclasses import dataclass

@dataclass
class TraceEvent:
    step: int
    node_id: str
    from_node_id: Optional[str]
    edge_relation: Optional[str]
    score: Optional[float]
    rationale: str
    direction: Optional[str]

# --------- Improved traversal ---------
def score_node_relevance(node_id: str, question: str, graph: nx.DiGraph = None) -> float:
    """Score how relevant a node is to the question."""
    if graph is None:
        graph = get_graph()
    
    if node_id not in graph.nodes:
        return 0.0
    
    node_data = graph.nodes[node_id]
    q_lower = question.lower()
    
    # Extract text from node
    label = node_data.get("label", "").lower()
    description = node_data.get("description", "").lower()
    node_id_lower = node_id.lower().replace("_", " ")
    
    # Count keyword matches
    score = 0.0
    keywords = re.findall(r'\b\w+\b', q_lower)
    
    for keyword in keywords:
        if len(keyword) < 3:  # Skip very short words
            continue
        if keyword in label:
            score += 2.0
        if keyword in description:
            score += 1.0
        if keyword in node_id_lower:
            score += 1.5
    
    return score

def find_start_nodes(question: str, max_candidates: int = 5, graph: nx.DiGraph = None) -> List[Tuple[str, float]]:
    """Find the most relevant starting nodes based on keyword matching."""
    if graph is None:
        graph = get_graph()
    
    q_lower = question.lower()
    candidates = []
    
    # Score all nodes
    for node_id in graph.nodes():
        score = score_node_relevance(node_id, question, graph)
        if score > 0:
            candidates.append((node_id, score))
    
    # Sort by score and return top candidates
    candidates.sort(key=lambda x: x[1], reverse=True)
    
    # If no good matches, try some fallback patterns
    if not candidates or candidates[0][1] < 0.5:
        fallbacks = []
        # Eating disorder patterns
        if "anorexia" in q_lower or "restrict" in q_lower:
            fallbacks.append(("anorexia_nervosa", 1.0))
        if "bulimia" in q_lower or ("binge" in q_lower and "purge" in q_lower):
            fallbacks.append(("bulimia_nervosa", 1.0))
        if "treatment" in q_lower or "therapy" in q_lower or "cbt" in q_lower:
            if "sepsis" not in q_lower:
                fallbacks.append(("cbt_ed", 1.0))
        if ("symptom" in q_lower or "sign" in q_lower) and "sepsis" not in q_lower:
            fallbacks.append(("body_image_distortion", 0.8))
        if "risk" in q_lower or "cause" in q_lower or "factor" in q_lower:
            if "sepsis" not in q_lower:
                fallbacks.append(("genetic_predisposition", 0.8))
        # Sepsis patterns
        if "sepsis" in q_lower or "septic" in q_lower:
            fallbacks.append(("sepsis", 1.0))
        if "sofa" in q_lower:
            fallbacks.append(("sofa_score", 1.0))
        if "qsofa" in q_lower or "quick sofa" in q_lower:
            fallbacks.append(("qsofa_score", 1.0))
        if "sirs" in q_lower:
            fallbacks.append(("sirs_criteria", 1.0))
        if "infection" in q_lower and "sepsis" in q_lower:
            fallbacks.append(("infection", 0.9))
        if "organ" in q_lower and "dysfunction" in q_lower:
            fallbacks.append(("organ_dysfunction", 0.9))
        if fallbacks:
            candidates = fallbacks + candidates
    
    return candidates[:max_candidates]

def get_neighbors_bidirectional(node_id: str, graph: nx.DiGraph = None) -> List[Tuple[str, str, Optional[str]]]:
    """Get both incoming and outgoing neighbors with their relations."""
    if graph is None:
        graph = get_graph()
    
    neighbors = []
    
    # Outgoing edges
    for _, neighbor, data in graph.out_edges(node_id, data=True):
        neighbors.append((neighbor, "out", data.get("relation")))
    
    # Incoming edges
    for source, _, data in graph.in_edges(node_id, data=True):
        neighbors.append((source, "in", data.get("relation")))
    
    return neighbors

def traverse_graph(question: str, max_steps: int = 30, graph: nx.DiGraph = None):
    """
    Improved traversal that:
    - Finds relevant start nodes via keyword matching
    - Traverses bidirectionally (both in and out edges)
    - Prioritizes relevant paths
    """
    if graph is None:
        graph = get_graph()
    
    start_candidates = find_start_nodes(question, graph=graph)
    
    if not start_candidates:
        return
    
    visited = set()
    step = 0
    
    # Priority queue: (node_id, from_node_id, direction, relation, relevance_score, depth)
    queue = []
    
    # Add start nodes to queue with high priority
    for node_id, score in start_candidates:
        if node_id not in visited:
            queue.append((node_id, None, None, None, score, 0))
    
    # Sort queue by relevance (higher score first)
    queue.sort(key=lambda x: x[4], reverse=True)
    
    while queue and step < max_steps:
        # Pop highest priority node
        node_id, from_id, direction, rel, relevance, depth = queue.pop(0)
        
        if node_id in visited:
            continue
        
        # Skip if depth is too deep (avoid going too far)
        if depth > 3:
            continue
            
        visited.add(node_id)
        
        node_data = graph.nodes[node_id]
        node_label = node_data.get("label", node_id)
        
        if from_id is None:
            rationale = f"Starting at '{node_label}' (relevance score: {relevance:.2f}) based on keyword matching."
        else:
            from_label = graph.nodes[from_id].get("label", from_id)
            direction_str = "following" if direction == "out" else "tracing back"
            rationale = f"{direction_str.capitalize()} from '{from_label}' to '{node_label}' via '{rel}' relation."
        
        event = TraceEvent(
            step=step,
            node_id=node_id,
            from_node_id=from_id,
            edge_relation=rel,
            score=relevance,
            rationale=rationale,
            direction=direction,
        )
        yield event
        step += 1
        
        # Add neighbors to queue with decreasing relevance
        neighbors = get_neighbors_bidirectional(node_id, graph)
        for neighbor_id, neighbor_dir, neighbor_rel in neighbors:
            if neighbor_id not in visited:
                # Calculate relevance for neighbor
                neighbor_score = score_node_relevance(neighbor_id, question, graph)
                # Decay relevance with depth
                neighbor_score *= (0.7 ** (depth + 1))
                queue.append((neighbor_id, node_id, neighbor_dir, neighbor_rel, neighbor_score, depth + 1))
        
        # Re-sort queue to maintain priority
        queue.sort(key=lambda x: x[4], reverse=True)

# --------- REST endpoints ---------
@app.get("/graphs")
async def list_graphs():
    """List all available graphs."""
    graphs = list_available_graphs()
    current = get_active_graph_name()
    return {
        "available_graphs": graphs,
        "current_graph": current,
        "graph_info": {name: get_graph_info(name) for name in graphs}
    }

@app.post("/graphs/{graph_name}/activate")
async def activate_graph(graph_name: str):
    """Switch to a different graph."""
    if set_active_graph(graph_name):
        return {
            "success": True,
            "current_graph": graph_name,
            "graph_info": get_graph_info(graph_name)
        }
    else:
        raise HTTPException(status_code=404, detail=f"Graph '{graph_name}' not found")

@app.get("/graphs/current")
async def get_current_graph():
    """Get information about the current graph."""
    name = get_active_graph_name()
    graph = get_graph()
    return {
        "name": name,
        "node_count": graph.number_of_nodes(),
        "edge_count": graph.number_of_edges(),
        "nodes": [
            {"id": node_id, "label": data.get("label", node_id), "type": data.get("type", "unknown")}
            for node_id, data in graph.nodes(data=True)
        ],
        "edges": [
            {"from": source, "to": target, "relation": data.get("relation", "related_to")}
            for source, target, data in graph.edges(data=True)
        ]
    }

# --------- WebSocket endpoint ---------
@app.websocket("/trace")
async def trace_endpoint(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            # Expect JSON: {"question": "...", "graph_name": "..." (optional)}
            data = await ws.receive_text()
            payload = json.loads(data)
            question = payload.get("question", "")
            graph_name = payload.get("graph_name", None)
            
            # Switch graph if requested
            if graph_name:
                if set_active_graph(graph_name):
                    await ws.send_text(json.dumps({
                        "type": "graph_switched",
                        "graph_name": graph_name
                    }))
                else:
                    await ws.send_text(json.dumps({
                        "type": "error",
                        "message": f"Graph '{graph_name}' not found"
                    }))
                    continue

            # Get current graph
            graph = get_graph()
            
            # You might send an event to clear the previous trace
            await ws.send_text(json.dumps({"type": "reset"}))

            # Stream trace events as we traverse
            for event in traverse_graph(question, graph=graph):
                await ws.send_text(json.dumps({
                    "type": "trace_step",
                    **asdict(event),
                }))
            # Once done, you can send a "done" message
            await ws.send_text(json.dumps({"type": "done"}))

    except WebSocketDisconnect:
        print("Client disconnected")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
