class LLMResponseError(Exception):
    """The LLM returned something we couldn't use."""

    def parse_reply(raw: str) -> dict:
        try:
            return json.loads(raw)
        except json.JSONDecodeError as e:
            raise LLMResponseError(f"bad JSON from model: {raw[:50]!r}") from e