from dataclasses import dataclass
import json

class LLMResponseError(Exception):
    pass

@dataclass
class Job:
    title: str
    salary_min: int

def parse_job(raw: str) -> Job:
    try:
        data = json.loads(raw)
        return Job(data["title"], data["salary_min"])
    except:
        raise LLMResponseError("model gave bad output")

job = parse_job('{"title": "AI Engineer", "salary_min": "not listed"}')
print (job)