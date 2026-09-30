from pydantic import BaseModel, ValidationError

class JobInfo(BaseModel):
    titles: str
    seniority: str
    salary_min: int

llm_output = '{"title": "AI Engineer", "Seniority: "mid", "salary_min": "not listed"}'

try:
    job = JobInfo.model_validate_json(llm_output)
except ValidationError as e:
    print(e)
