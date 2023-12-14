from typing import Union
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app=app)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="images"), name="images")