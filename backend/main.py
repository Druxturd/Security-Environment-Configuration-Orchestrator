from fastapi import FastAPI
from routes import harden, patch, file

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(harden.router)
app.include_router(patch.router)
app.include_router(file.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)