"""
Graph loader module to support multiple knowledge graphs.
Can load from Python graph definitions or TTL files.
"""
import networkx as nx
from typing import Dict, Optional
import os

# Import graph definitions
from graph import G as eating_disorder_graph
from sepsis_graph import G as sepsis_graph

# Dictionary to store all available graphs
AVAILABLE_GRAPHS: Dict[str, nx.DiGraph] = {
    "eating_disorder": eating_disorder_graph,
    "sepsis": sepsis_graph,
}

# Current active graph (default to eating disorder)
_current_graph = eating_disorder_graph
_current_graph_name = "eating_disorder"

def get_graph(graph_name: str = None) -> Optional[nx.DiGraph]:
    """Get a graph by name, or return current graph if name is None."""
    if graph_name is None:
        return _current_graph
    return AVAILABLE_GRAPHS.get(graph_name)

def set_active_graph(graph_name: str) -> bool:
    """Set the active graph. Returns True if successful."""
    global _current_graph, _current_graph_name
    if graph_name in AVAILABLE_GRAPHS:
        _current_graph = AVAILABLE_GRAPHS[graph_name]
        _current_graph_name = graph_name
        return True
    return False

def get_active_graph_name() -> str:
    """Get the name of the currently active graph."""
    return _current_graph_name

def list_available_graphs() -> list:
    """List all available graph names."""
    return list(AVAILABLE_GRAPHS.keys())

def get_graph_info(graph_name: str = None) -> Dict:
    """Get metadata about a graph."""
    graph = get_graph(graph_name)
    if graph is None:
        return {}
    
    return {
        "name": graph_name or _current_graph_name,
        "node_count": graph.number_of_nodes(),
        "edge_count": graph.number_of_edges(),
    }

