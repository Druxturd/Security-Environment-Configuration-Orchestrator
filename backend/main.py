import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from backend.routes import file, harden, patch

app = FastAPI()

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))


@app.get("/")
def read_root():
    return {"status": "ok"}


app.include_router(harden.router)
app.include_router(patch.router)
app.include_router(file.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)
