import ollama
import json
import os



def ats_extractor(resume_text):
    """
    Parses resume text using Gemini 2.0 Flash to extract structured JSON data.
    """
    
    system_prompt = f"""
    You are an expert ATS (Applicant Tracking System). 
    Extract the following entities from the provided resume text into a clean JSON format:
    - Name
    - Email
    - LinkedIn (URL)
    - GitHub (URL)
    - Companies (List of past employers)
    - Projects (Brief list of project titles)
    - Research (Any publications or research mentions)
    - Skills (List of technical skills)

    Resume Text:
    {resume_text}

    Return ONLY valid JSON.
    """

    try:
        response = ollama.chat(
            model='llama3.2',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': f"Resume text:\n{resume_text}"}
            ],
            format='json',
            options={'temperature': 0}
        )
        
        # response.text will contain a clean JSON string because of response_mime_type
        return json.loads(response['message']['content'])
        
    except Exception as e:
        print(f"Extraction Error: {e}")
        return {
            "Name": "Error",
            "Email": "N/A",
            "LinkedIn": [],
            "GitHub": [],
            "Companies": [],
            "Projects": [],
            "Research": [],
            "Skills": ["Service Error: " + str(e)]
        }