from fastapi import FastAPI
from routes import harden, patch, file, test_ansible_runner

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(harden.router)
app.include_router(patch.router)
app.include_router(file.router)
app.include_router(test_ansible_runner.router) # testing

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)