from fastapi import FastAPI

app = FastAPI()

diseases = {
    "flu": "fever, cough, sore throat, fatigue",
    "cold": "runny or stuffy nose, sore throat, sneezing, mild cough",
    "pneumonia": "high fever, chills, cough with phlegm, chest pain, difficulty breathing",
    "bronchitis": "persistent cough, chest discomfort, fatigue, shortness of breath, fever",
    "asthma": "shortness of breath, wheezing, chest tightness, coughing, difficulty sleeping due to coughing or wheezing",
    "hypertension": "headache, fatigue, chest pain, irregular heartbeat, vision problems",
    "diabetes": "increased thirst, frequent urination, extreme hunger, unexplained weight loss, fatigue, irritability",
    "allergies": "sneezing, runny or stuffy nose, itchy or watery eyes, itching of the throat or ears, rash or hives",
    "heart disease": "chest pain or discomfort, shortness of breath, nausea, lightheadedness, cold sweats",
    "stroke": "sudden numbness or weakness in the face, arm, or leg, confusion, trouble speaking or understanding speech, trouble seeing, dizziness, loss of balance or coordination",
    "anxiety disorders": "excessive worrying, restlessness, fatigue, difficulty concentrating, irritability, muscle tension, sleep disturbances",
    "depression": "persistent sadness, loss of interest or pleasure in activities, changes in appetite or weight, sleep disturbances, fatigue, feelings of worthlessness or guilt",
    "migraine": "throbbing headache, usually on one side of the head, nausea, vomiting, sensitivity to light and sound, visual disturbances",
    "irritable bowel syndrome (IBS)": "abdominal pain or discomfort, bloating, gas, diarrhea or constipation, mucus in the stool",
    "acid reflux": "heartburn, regurgitation of sour liquid or food, chest pain, difficulty swallowing, chronic cough, hoarseness",
    "endometriosis": "pelvic pain, painful periods, pain during intercourse, infertility, heavy menstrual bleeding, fatigue",
    "chronic fatigue syndrome": "persistent fatigue that is not relieved by rest, muscle pain, joint pain, headaches, impaired memory or concentration",
    "fibromyalgia": "widespread muscle pain, fatigue, sleep disturbances, headaches, cognitive difficulties, numbness or tingling in hands and feet",
    "thyroid": "fatigue, weight gain or loss, sensitivity to cold or heat, changes in heart rate, dry skin, brittle nails, hair loss",
    "type 2 diabetes": "increased thirst, frequent urination, fatigue, blurred vision, slow-healing sores or cuts, tingling or numbness in hands or feet",
    "inflammatory bowel disease": "abdominal pain, diarrhea, rectal bleeding, weight loss, fatigue, fever",
    "chronic sinusitis": "facial pain or pressure, nasal congestion, drainage of thick, discolored mucus, cough, reduced sense of smell or taste",
    "sleep disorders": "difficulty falling or staying asleep, excessive daytime sleepiness, loud snoring, gasping or choking during sleep",
    "bipolar disorder": "periods of depression alternating with periods of elevated mood (mania or hypomania), changes in energy and activity levels, changes in sleep patterns",
    "substance abuse disorders": "compulsive use of drugs or alcohol despite negative consequences, tolerance, withdrawal symptoms, inability to control use",
    "eating disorders": "extreme food restriction or binge eating followed by purging, excessive exercise, preoccupation with body weight and shape",
    "pcos": "irregular periods, excess androgen levels (resulting in acne, excess facial or body hair, and male-pattern baldness), polycystic ovaries, weight gain, infertility, insulin resistance, mood changes",
    "osteoporosis": "bone fractures that occur more easily than expected, back pain, loss of height over time, stooped posture",
    "arthritis": "joint pain, stiffness, swelling, decreased range of motion",
    "chronic obstructive pulmonary disease": "shortness of breath, chronic cough, wheezing, tightness in the chest, frequent respiratory infections",
    "gastroesophageal reflux disease": "heartburn, regurgitation of food or sour liquid, sensation of a lump in the throat, difficulty swallowing",
    "multiple sclerosis": "fatigue, numbness or weakness in one or more limbs, tremors, lack of coordination, blurred or double vision, slurred speech",
    "Parkinson's disease": "tremor, stiffness, slowed movement, impaired balance, voice changes",
    "Alzheimer's disease": "memory loss, confusion, difficulty completing familiar tasks, challenges with planning or problem-solving, mood swings",
    "osteoarthritis": "joint pain, stiffness, swelling, decreased range of motion",
    "osteoporosis": "bone fractures that occur more easily than expected, back pain, loss of height over time, stooped posture",
    "schizophrenia": "hallucinations, delusions, disorganized thinking, lack of emotion, social withdrawal",
    "panic disorder": "sudden and repeated attacks of fear, feeling of being out of control during a panic attack, intense worry about when the next attack will happen",
    "post-traumatic stress disorder": "flashbacks, nightmares, severe anxiety, uncontrollable thoughts about the traumatic event, avoidance of situations that remind one of the event",
    "endometrial cancer": "unusual vaginal bleeding, pelvic pain, pain during intercourse, difficulty urinating or defecating",
    "ovarian cancer": "abdominal bloating or swelling, pelvic pain or pressure, difficulty eating or feeling full quickly, urinary symptoms",
    "colon cancer": "changes in bowel habits, rectal bleeding or blood in the stool, persistent abdominal discomfort, unexplained weight loss",
    "breast cancer": "lump or mass in the breast or underarm, changes in breast size, shape, or appearance, nipple changes or discharge",
    "lung cancer": "persistent cough, chest pain, shortness of breath, wheezing, hoarseness, coughing up blood",
    "prostate cancer": "frequent urination, especially at night, difficulty starting or stopping urination, weak or interrupted urinary stream, blood in the urine or semen",
    "skin cancer": "changes in the size, shape, or color of a mole or other skin lesion, a sore that doesn't heal, new growths or lumps on the skin",
    "celiac disease": "digestive symptoms (diarrhea, constipation, bloating), fatigue, weight loss, skin rash (dermatitis herpetiformis), depression or anxiety",
    "Crohn's disease": "abdominal pain, diarrhea, weight loss, fatigue, fever, mouth sores, reduced appetite",
    "ulcerative colitis": "rectal bleeding, abdominal cramps, diarrhea, urgency to defecate, fatigue, weight loss, fever",
    "lupus": "joint pain and swelling, fatigue, fever, skin rash (especially on the face), chest pain, hair loss, sensitivity to sunlight",
    "rheumatoid arthritis": "joint pain and swelling, morning stiffness, fatigue, fever, weight loss, joint deformity over time",
    "fibroids": "heavy menstrual bleeding, prolonged periods, pelvic pain or pressure, frequent urination, constipation, back or leg pain",
    "endometrial hyperplasia": "abnormal uterine bleeding, heavy or prolonged periods, bleeding between periods, pelvic pain or pressure, frequent urination",
    "menopause": "irregular periods, hot flashes, night sweats, vaginal dryness, sleep disturbances, mood swings",
    "obstructive sleep apnea": "loud snoring, observed episodes of stopped breathing during sleep, abrupt awakenings accompanied by shortness of breath, daytime sleepiness, difficulty concentrating",
    "restless legs syndrome": "uncomfortable sensations in the legs (itching, tingling, crawling), an urge to move the legs, symptoms worsen at rest or in the evening, relief with movement",
    "fibrocystic breast changes": "breast lumps or areas of thickening, breast pain or discomfort, tenderness that fluctuates with the menstrual cycle",
    "gallstones": "abdominal pain, nausea, vomiting, bloating, indigestion, intolerance to fatty foods, yellowing of the skin or eyes (jaundice)",
    "pancreatitis": "abdominal pain (often severe and radiating to the back), nausea, vomiting, fever, rapid pulse, tenderness of the abdomen",
    "gout": "sudden, severe pain in a joint (often the big toe), swelling, redness, warmth, tenderness, limited range of motion",
    "diverticulitis": "abdominal pain (usually on the left side), fever, nausea, vomiting, change in bowel habits, bloating, constipation or diarrhea",
    "ulcers": "burning stomach pain, bloating, belching, nausea, vomiting, dark stools, unexplained weight loss"
}


@app.get("/symptoms/{disease}")
async def get_symptoms(disease: str):
    if disease.lower() in diseases:
        symptoms = diseases[disease.lower()]
        return {"disease": disease, "symptoms": symptoms}
    else:
        return {"error": f"I'm sorry, I don't have information on {disease}."}
