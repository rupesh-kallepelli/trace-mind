from app.llm.provider import call_llm_json

async def generate_query(issue: str):
    prompt = f"""
    Extract service and keywords from the issue.

    Issue: {issue}

    Return JSON:
    {{
        "service": "",
        "keywords": []
    }}
    """

    return await call_llm_json(prompt)
