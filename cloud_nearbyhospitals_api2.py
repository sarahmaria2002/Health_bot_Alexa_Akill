from fastapi import FastAPI
from typing import Dict

app = FastAPI()

nearby_hospital = {
    "Christian Medical College (CMC), Vellore": "Ida Scudder Rd, Vellore, Tamil Nadu",
    "Sri Ramachandra Medical Centre": "Porur, Chennai, Tamil Nadu",
    "Apollo Hospitals": "Greams Road, Chennai, Tamil Nadu",
    "Fortis Malar Hospital": "Adyar, Chennai, Tamil Nadu",
    "MIOT International": "Manapakkam, Chennai, Tamil Nadu",
    "Global Hospitals": "Perumbakkam, Chennai, Tamil Nadu",
    "Kauvery Hospital": "Alwarpet, Chennai, Tamil Nadu",
    "SIMS Hospital": "Vadapalani, Chennai, Tamil Nadu",
    "Frontier Lifeline Hospital": "Mogappair, Chennai, Tamil Nadu",
    "Government General Hospital": "Park Town, Chennai, Tamil Nadu",
    "Madras Medical Mission": "Mogappair, Chennai, Tamil Nadu",
    "Billroth Hospitals": "Shenoy Nagar, Chennai, Tamil Nadu"
}

@app.get("/nearby_hospitals")
def get_nearby_hospitals() -> Dict[str, str]:
    return nearby_hospital
