from fastapi import FastAPI, Request, Response


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    return {"health status": "HEALTHY"}

