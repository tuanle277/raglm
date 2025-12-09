import networkx as nx

G = nx.DiGraph()

# Diagnosis nodes
G.add_node("anorexia_nervosa", 
           label="Anorexia Nervosa", 
           type="diagnosis", 
           description="An eating disorder characterized by restriction of energy intake, intense fear of gaining weight, and disturbance in body image")

G.add_node("anorexia_restricting_type",
           label="Anorexia Nervosa Restricting Type",
           type="diagnosis",
           description="Subtype where weight loss is accomplished primarily through dieting, fasting, or excessive exercise")

G.add_node("anorexia_binge_purge_type",
           label="Anorexia Nervosa Binge-Eating/Purging Type",
           type="diagnosis",
           description="Subtype where the individual has engaged in recurrent episodes of binge eating or purging behavior")

G.add_node("bulimia_nervosa",
           label="Bulimia Nervosa",
           type="diagnosis",
           description="Eating disorder characterized by recurrent episodes of binge eating followed by compensatory behaviors")

G.add_node("binge_eating_disorder",
           label="Binge Eating Disorder",
           type="diagnosis",
           description="Eating disorder characterized by recurrent episodes of eating large amounts of food without compensatory behaviors")

G.add_node("osfed",
           label="Other Specified Feeding or Eating Disorder",
           type="diagnosis",
           description="Eating disorder that does not meet full criteria for anorexia, bulimia, or binge eating disorder")

# Symptom nodes
G.add_node("body_image_distortion", 
           label="Body image distortion", 
           type="symptom",
           description="Distorted perception of one's body size, shape, or weight")

G.add_node("fear_of_weight_gain",
           label="Fear of weight gain",
           type="symptom",
           description="Intense, persistent fear of gaining weight or becoming fat")

G.add_node("restrictive_eating",
           label="Restrictive eating",
           type="symptom",
           description="Severely limiting food intake, often below caloric needs")

G.add_node("excessive_exercise",
           label="Excessive exercise",
           type="symptom",
           description="Compulsive, driven exercise that interferes with daily functioning")

G.add_node("amenorrhea",
           label="Amenorrhea",
           type="symptom",
           description="Absence of menstrual periods, often associated with low body weight")

G.add_node("binge_episodes",
           label="Binge episodes",
           type="symptom",
           description="Eating an unusually large amount of food in a discrete period with loss of control")

G.add_node("purging_behavior",
           label="Purging behavior",
           type="symptom",
           description="Self-induced vomiting or misuse of laxatives, diuretics, or enemas")

G.add_node("preoccupation_with_food",
           label="Preoccupation with food",
           type="symptom",
           description="Excessive thoughts about food, calories, and eating")

G.add_node("perfectionism",
           label="Perfectionism",
           type="symptom",
           description="Rigid standards and excessive self-criticism")

G.add_node("low_self_esteem",
           label="Low self-esteem",
           type="symptom",
           description="Negative self-evaluation and feelings of worthlessness")

# Treatment nodes
G.add_node("cbt_ed", 
           label="CBT-E", 
           type="treatment",
           description="Enhanced Cognitive Behavioral Therapy for eating disorders")

G.add_node("fbt",
           label="Family-Based Treatment",
           type="treatment",
           description="Maudsley method, family therapy approach for adolescents with anorexia")

G.add_node("ipt",
           label="Interpersonal Psychotherapy",
           type="treatment",
           description="Therapy focusing on interpersonal relationships and social functioning")

G.add_node("dbt",
           label="Dialectical Behavior Therapy",
           type="treatment",
           description="Therapy combining cognitive-behavioral techniques with mindfulness")

G.add_node("act",
           label="Acceptance and Commitment Therapy",
           type="treatment",
           description="Therapy focusing on acceptance, mindfulness, and values-based action")

G.add_node("nutritional_counseling",
           label="Nutritional counseling",
           type="treatment",
           description="Dietary intervention and meal planning support")

G.add_node("medical_monitoring",
           label="Medical monitoring",
           type="treatment",
           description="Regular medical check-ups to monitor physical health")

G.add_node("inpatient_treatment",
           label="Inpatient treatment",
           type="treatment",
           description="Hospital-based treatment for severe cases requiring medical stabilization")

G.add_node("partial_hospitalization",
           label="Partial hospitalization",
           type="treatment",
           description="Day treatment program providing intensive therapy while living at home")

# Comorbidity nodes
G.add_node("major_depression",
           label="Major Depressive Disorder",
           type="comorbidity",
           description="Mood disorder characterized by persistent sadness and loss of interest")

G.add_node("anxiety_disorder",
           label="Anxiety Disorder",
           type="comorbidity",
           description="Group of disorders characterized by excessive fear and anxiety")

G.add_node("ocd",
           label="Obsessive-Compulsive Disorder",
           type="comorbidity",
           description="Disorder characterized by obsessions and compulsions")

G.add_node("ptsd",
           label="Post-Traumatic Stress Disorder",
           type="comorbidity",
           description="Disorder that can develop after exposure to traumatic events")

G.add_node("substance_use_disorder",
           label="Substance Use Disorder",
           type="comorbidity",
           description="Problematic pattern of substance use leading to impairment")

# Risk factor nodes
G.add_node("genetic_predisposition",
           label="Genetic predisposition",
           type="risk_factor",
           description="Family history and genetic factors increasing vulnerability")

G.add_node("societal_pressure",
           label="Societal pressure",
           type="risk_factor",
           description="Cultural emphasis on thinness and appearance")

G.add_node("childhood_trauma",
           label="Childhood trauma",
           type="risk_factor",
           description="Adverse childhood experiences that increase risk")

G.add_node("personality_traits",
           label="Personality traits",
           type="risk_factor",
           description="Traits like perfectionism, neuroticism, and low self-esteem")

G.add_node("dieting_history",
           label="History of dieting",
           type="risk_factor",
           description="Previous attempts at weight loss or restrictive eating")

# Medical complication nodes
G.add_node("osteoporosis",
           label="Osteoporosis",
           type="complication",
           description="Bone density loss due to nutritional deficiencies and low estrogen")

G.add_node("cardiac_complications",
           label="Cardiac complications",
           type="complication",
           description="Bradycardia, hypotension, and arrhythmias from malnutrition")

G.add_node("electrolyte_imbalance",
           label="Electrolyte imbalance",
           type="complication",
           description="Abnormal levels of sodium, potassium, and other electrolytes")

G.add_node("gastrointestinal_issues",
           label="Gastrointestinal issues",
           type="complication",
           description="Delayed gastric emptying, constipation, and gastroparesis")

G.add_node("anemia",
           label="Anemia",
           type="complication",
           description="Low red blood cell count due to nutritional deficiencies")

# Diagnostic criteria nodes
G.add_node("dsm5_criteria",
           label="DSM-5 Criteria",
           type="diagnostic_criteria",
           description="Diagnostic and Statistical Manual criteria for eating disorders")

G.add_node("bmi_criteria",
           label="BMI criteria",
           type="diagnostic_criteria",
           description="Body Mass Index thresholds used in diagnosis")

# Outcome nodes
G.add_node("recovery",
           label="Recovery",
           type="outcome",
           description="Successful treatment outcome with restored physical and psychological health")

G.add_node("relapse",
           label="Relapse",
           type="outcome",
           description="Return of symptoms after a period of improvement")

G.add_node("chronic_illness",
           label="Chronic illness",
           type="outcome",
           description="Long-term persistence of eating disorder symptoms")

# Edges capturing semantic relations

# Diagnosis relationships
G.add_edge("anorexia_restricting_type", "anorexia_nervosa", relation="subtype_of")
G.add_edge("anorexia_binge_purge_type", "anorexia_nervosa", relation="subtype_of")
G.add_edge("anorexia_nervosa", "bulimia_nervosa", relation="related_disorder")
G.add_edge("anorexia_nervosa", "binge_eating_disorder", relation="related_disorder")
G.add_edge("anorexia_nervosa", "osfed", relation="related_disorder")

# Symptom to diagnosis relationships
G.add_edge("body_image_distortion", "anorexia_nervosa", relation="core_feature")
G.add_edge("fear_of_weight_gain", "anorexia_nervosa", relation="core_feature")
G.add_edge("restrictive_eating", "anorexia_nervosa", relation="core_feature")
G.add_edge("excessive_exercise", "anorexia_nervosa", relation="common_symptom")
G.add_edge("amenorrhea", "anorexia_nervosa", relation="associated_symptom")
G.add_edge("binge_episodes", "anorexia_binge_purge_type", relation="core_feature")
G.add_edge("purging_behavior", "anorexia_binge_purge_type", relation="core_feature")
G.add_edge("purging_behavior", "bulimia_nervosa", relation="core_feature")
G.add_edge("preoccupation_with_food", "anorexia_nervosa", relation="common_symptom")
G.add_edge("perfectionism", "anorexia_nervosa", relation="risk_factor")
G.add_edge("low_self_esteem", "anorexia_nervosa", relation="risk_factor")

# Treatment relationships
G.add_edge("cbt_ed", "anorexia_nervosa", relation="evidence_based_treatment")
G.add_edge("cbt_ed", "bulimia_nervosa", relation="evidence_based_treatment")
G.add_edge("fbt", "anorexia_nervosa", relation="evidence_based_treatment")
G.add_edge("ipt", "bulimia_nervosa", relation="evidence_based_treatment")
G.add_edge("dbt", "anorexia_nervosa", relation="treatment_option")
G.add_edge("dbt", "bulimia_nervosa", relation="treatment_option")
G.add_edge("act", "anorexia_nervosa", relation="treatment_option")
G.add_edge("nutritional_counseling", "anorexia_nervosa", relation="adjunctive_treatment")
G.add_edge("medical_monitoring", "anorexia_nervosa", relation="essential_component")
G.add_edge("inpatient_treatment", "anorexia_nervosa", relation="indicated_for_severe_cases")
G.add_edge("partial_hospitalization", "anorexia_nervosa", relation="treatment_setting")

# Comorbidity relationships
G.add_edge("major_depression", "anorexia_nervosa", relation="common_comorbidity")
G.add_edge("anxiety_disorder", "anorexia_nervosa", relation="common_comorbidity")
G.add_edge("ocd", "anorexia_nervosa", relation="common_comorbidity")
G.add_edge("ptsd", "anorexia_nervosa", relation="associated_comorbidity")
G.add_edge("substance_use_disorder", "anorexia_nervosa", relation="associated_comorbidity")

# Risk factor relationships
G.add_edge("genetic_predisposition", "anorexia_nervosa", relation="increases_risk")
G.add_edge("societal_pressure", "anorexia_nervosa", relation="environmental_risk_factor")
G.add_edge("childhood_trauma", "anorexia_nervosa", relation="increases_risk")
G.add_edge("personality_traits", "anorexia_nervosa", relation="increases_risk")
G.add_edge("dieting_history", "anorexia_nervosa", relation="precursor")

# Complication relationships
G.add_edge("anorexia_nervosa", "osteoporosis", relation="can_cause")
G.add_edge("anorexia_nervosa", "cardiac_complications", relation="can_cause")
G.add_edge("anorexia_nervosa", "electrolyte_imbalance", relation="can_cause")
G.add_edge("purging_behavior", "electrolyte_imbalance", relation="can_cause")
G.add_edge("anorexia_nervosa", "gastrointestinal_issues", relation="can_cause")
G.add_edge("anorexia_nervosa", "anemia", relation="can_cause")
G.add_edge("restrictive_eating", "osteoporosis", relation="contributes_to")
G.add_edge("restrictive_eating", "cardiac_complications", relation="contributes_to")

# Diagnostic criteria relationships
G.add_edge("dsm5_criteria", "anorexia_nervosa", relation="defines")
G.add_edge("bmi_criteria", "anorexia_nervosa", relation="diagnostic_indicator")
G.add_edge("body_image_distortion", "dsm5_criteria", relation="required_for_diagnosis")
G.add_edge("fear_of_weight_gain", "dsm5_criteria", relation="required_for_diagnosis")
G.add_edge("restrictive_eating", "dsm5_criteria", relation="required_for_diagnosis")

# Outcome relationships
G.add_edge("cbt_ed", "recovery", relation="can_lead_to")
G.add_edge("fbt", "recovery", relation="can_lead_to")
G.add_edge("anorexia_nervosa", "recovery", relation="can_result_in")
G.add_edge("anorexia_nervosa", "relapse", relation="can_result_in")
G.add_edge("anorexia_nervosa", "chronic_illness", relation="can_result_in")
G.add_edge("recovery", "relapse", relation="can_precede")

# Cross-connections
G.add_edge("perfectionism", "restrictive_eating", relation="drives")
G.add_edge("low_self_esteem", "body_image_distortion", relation="exacerbates")
G.add_edge("anxiety_disorder", "restrictive_eating", relation="can_manifest_as")
G.add_edge("ocd", "preoccupation_with_food", relation="can_manifest_as")
G.add_edge("major_depression", "low_self_esteem", relation="associated_with")
G.add_edge("nutritional_counseling", "medical_monitoring", relation="complements")
G.add_edge("inpatient_treatment", "medical_monitoring", relation="includes")
