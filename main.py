from fastapi import FastAPI

app = FastAPI()

@app.get("/teams/status")
def status():
    return {"message": "Team Service is running ✅"}
