# main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from json import loads

app = FastAPI()

@app.get("/base")
async def root():
    #return { "http://smbc-comics.com": " \n\n \n\n \n \n\nYOU KNO"}
    with open('data', 'r') as f:
        return loads(f.read())


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
