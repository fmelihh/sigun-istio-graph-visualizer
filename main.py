import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/callback")
async def callback(request: Request):
    body = await request.body()
    print(f"Received mirrored request: {request.method} {request.url}")
    print(f"Headers: {dict(request.headers)}")
    print(f"Body: {body}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
