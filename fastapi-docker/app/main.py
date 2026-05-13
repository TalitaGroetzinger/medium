# run in docker-example using: 
# uvicorn app.main:app or fastapi run app/main.py --port 80 --reload

from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from app.config import config

app = FastAPI(title="DockerExample", version="1.0.0")


# redirect user to /docs
@app.get("/")
async def docs_redirect():
    return RedirectResponse(url="/docs")

@app.get("/hello-world")
async def get_hello_world():
    return {"message": "Hello World in {0} mode!".format(config.ENV)}