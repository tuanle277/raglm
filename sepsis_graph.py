import networkx as nx

G = nx.DiGraph()

# Core diagnosis nodes
G.add_node("sepsis",
           label="Sepsis",
           type="diagnosis",
           description="Life-threatening organ dysfunction caused by a dysregulated host response to infection")

G.add_node("septic_shock",
           label="Septic Shock",
           type="diagnosis",
           description="Sepsis with persisting hypotension requiring vasopressors to maintain MAP ≥65 mmHg and having a serum lactate level >2 mmol/L despite adequate volume resuscitation")

G.add_node("infection",
           label="Infection",
           type="condition",
           description="Invasion and multiplication of microorganisms in body tissues")

G.add_node("organ_dysfunction",
           label="Organ Dysfunction",
           type="condition",
           description="Abnormal organ function in response to infection")

# Diagnostic criteria systems
G.add_node("sofa_score",
           label="SOFA Score",
           type="diagnostic_criteria",
           description="Sequential Organ Failure Assessment score - used to assess organ dysfunction in sepsis")

G.add_node("qsofa_score",
           label="qSOFA Score",
           type="diagnostic_criteria",
           description="Quick SOFA score - rapid bedside assessment for sepsis")

G.add_node("sirs_criteria",
           label="SIRS Criteria",
           type="diagnostic_criteria",
           description="Systemic Inflammatory Response Syndrome criteria - older diagnostic system")

# SOFA Score components
G.add_node("respiratory_sofa",
           label="Respiratory SOFA",
           type="sofa_component",
           description="Respiratory component of SOFA score based on PaO2/FiO2 ratio")

G.add_node("coagulation_sofa",
           label="Coagulation SOFA",
           type="sofa_component",
           description="Coagulation component of SOFA score based on platelet count")

G.add_node("liver_sofa",
           label="Liver SOFA",
           type="sofa_component",
           description="Liver component of SOFA score based on bilirubin level")

G.add_node("cardiovascular_sofa",
           label="Cardiovascular SOFA",
           type="sofa_component",
           description="Cardiovascular component of SOFA score based on mean arterial pressure")

G.add_node("cns_sofa",
           label="CNS SOFA",
           type="sofa_component",
           description="Central Nervous System component of SOFA score based on Glasgow Coma Scale")

G.add_node("renal_sofa",
           label="Renal SOFA",
           type="sofa_component",
           description="Renal component of SOFA score based on creatinine level or urine output")

# Clinical parameters
G.add_node("pao2_fio2_ratio",
           label="PaO2/FiO2 Ratio",
           type="clinical_parameter",
           description="Ratio of arterial oxygen partial pressure to fractional inspired oxygen")

G.add_node("platelet_count",
           label="Platelet Count",
           type="clinical_parameter",
           description="Number of platelets per microliter of blood")

G.add_node("bilirubin_level",
           label="Bilirubin Level",
           type="clinical_parameter",
           description="Total bilirubin concentration in blood")

G.add_node("mean_arterial_pressure",
           label="Mean Arterial Pressure (MAP)",
           type="clinical_parameter",
           description="Average arterial pressure during one cardiac cycle")

G.add_node("glasgow_coma_scale",
           label="Glasgow Coma Scale (GCS)",
           type="clinical_parameter",
           description="Neurological scale for assessing level of consciousness")

G.add_node("creatinine_level",
           label="Creatinine Level",
           type="clinical_parameter",
           description="Serum creatinine concentration indicating renal function")

G.add_node("urine_output",
           label="Urine Output",
           type="clinical_parameter",
           description="Volume of urine produced per unit time")

# qSOFA components
G.add_node("altered_mental_status",
           label="Altered Mental Status",
           type="clinical_parameter",
           description="GCS < 15 or confusion")

G.add_node("respiratory_rate",
           label="Respiratory Rate",
           type="clinical_parameter",
           description="Number of breaths per minute")

G.add_node("systolic_blood_pressure",
           label="Systolic Blood Pressure",
           type="clinical_parameter",
           description="Maximum arterial pressure during cardiac contraction")

# SIRS criteria components
G.add_node("body_temperature",
           label="Body Temperature",
           type="clinical_parameter",
           description="Core body temperature")

G.add_node("heart_rate",
           label="Heart Rate",
           type="clinical_parameter",
           description="Number of heartbeats per minute")

G.add_node("white_blood_cell_count",
           label="White Blood Cell Count",
           type="clinical_parameter",
           description="Number of white blood cells per microliter of blood")

# Edges - Core relationships
G.add_edge("infection", "sepsis", relation="required_for")
G.add_edge("organ_dysfunction", "sepsis", relation="required_for")
G.add_edge("sepsis", "septic_shock", relation="can_progress_to")

# SOFA Score relationships
G.add_edge("sofa_score", "sepsis", relation="assesses")
G.add_edge("sofa_score", "respiratory_sofa", relation="has_component")
G.add_edge("sofa_score", "coagulation_sofa", relation="has_component")
G.add_edge("sofa_score", "liver_sofa", relation="has_component")
G.add_edge("sofa_score", "cardiovascular_sofa", relation="has_component")
G.add_edge("sofa_score", "cns_sofa", relation="has_component")
G.add_edge("sofa_score", "renal_sofa", relation="has_component")

# SOFA component to clinical parameter relationships
G.add_edge("respiratory_sofa", "pao2_fio2_ratio", relation="uses")
G.add_edge("coagulation_sofa", "platelet_count", relation="uses")
G.add_edge("liver_sofa", "bilirubin_level", relation="uses")
G.add_edge("cardiovascular_sofa", "mean_arterial_pressure", relation="uses")
G.add_edge("cns_sofa", "glasgow_coma_scale", relation="uses")
G.add_edge("renal_sofa", "creatinine_level", relation="uses")
G.add_edge("renal_sofa", "urine_output", relation="uses")

# qSOFA relationships
G.add_edge("qsofa_score", "sepsis", relation="screens_for")
G.add_edge("qsofa_score", "altered_mental_status", relation="includes")
G.add_edge("qsofa_score", "respiratory_rate", relation="includes")
G.add_edge("qsofa_score", "systolic_blood_pressure", relation="includes")

# SIRS criteria relationships
G.add_edge("sirs_criteria", "sepsis", relation="older_criteria_for")
G.add_edge("sirs_criteria", "body_temperature", relation="includes")
G.add_edge("sirs_criteria", "heart_rate", relation="includes")
G.add_edge("sirs_criteria", "respiratory_rate", relation="includes")
G.add_edge("sirs_criteria", "white_blood_cell_count", relation="includes")

# Clinical parameter relationships
G.add_edge("organ_dysfunction", "respiratory_sofa", relation="measured_by")
G.add_edge("organ_dysfunction", "coagulation_sofa", relation="measured_by")
G.add_edge("organ_dysfunction", "liver_sofa", relation="measured_by")
G.add_edge("organ_dysfunction", "cardiovascular_sofa", relation="measured_by")
G.add_edge("organ_dysfunction", "cns_sofa", relation="measured_by")
G.add_edge("organ_dysfunction", "renal_sofa", relation="measured_by")

