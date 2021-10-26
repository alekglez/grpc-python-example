# -*- coding: utf-8 -*-

import json
from datetime import datetime, timedelta

import uvicorn
from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI()


@app.get("/health")
def health():
    return {"Hello": "World"}


@app.post("/ticket")
async def manage_tickets(request: Request,):
    points = json.loads(await request.body()).get("story_points")
    expected_dateline = datetime.utcnow() + timedelta(days=points)
    return expected_dateline.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3001)
