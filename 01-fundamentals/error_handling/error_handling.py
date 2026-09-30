import json
import logging 

raw = 'Here is your JSON: {"name": "Neil"}'

try: 
    data = json.loads(raw)
except json.JSONDecodeError as e:
    logging.warning("LLM returned invalid JSON: %s", e)
    data = None