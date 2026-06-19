from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

def get_health_prediction(full_name, dob, glucose, haemoglobin, cholesterol):
    
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    prompt = f"""
    You are a medical AI assistant. Based on the following patient blood test results, 
    provide a brief health risk assessment in 2-3 sentences. 
    Be clear, professional, and mention possible health conditions if values are abnormal.
    
    Patient Name: {full_name}
    Date of Birth: {dob}
    Blood Test Results:
    - Glucose: {glucose} mg/dL (Normal: 70-100 mg/dL)
    - Haemoglobin: {haemoglobin} g/dL (Normal: Men 13.5-17.5, Women 12-15.5)
    - Cholesterol: {cholesterol} mg/dL (Normal: below 200 mg/dL)
    
    Provide health risk assessment only. No disclaimers needed.
    """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    
    return response.choices[0].message.content