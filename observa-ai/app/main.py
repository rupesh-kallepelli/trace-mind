from fastapi import FastAPI
from app.agent import graph

app = FastAPI()


@app.get("/analyze")
def analyze(issue: str):
    result = graph.invoke({
        "issue": issue,
        "keyword": "",
        "logs": [],
        "analysis": "",
        "decision": "",
        "result": ""
    })

    return result