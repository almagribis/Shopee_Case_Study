import json, re

def extract_json(text:str):    
    clean = re.sub(r"```json|```", "", text).strip()
    clean = clean.encode('utf-8').decode('unicode_escape')
    return json.loads(clean)
