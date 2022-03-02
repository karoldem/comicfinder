from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

base = {"http://smbc-comics.com": "  \n\n \n\n \n  \n\nYOU KNOW HOW YOU SIT ON THE COUCH,\nEATING SNACKS, USING A CONTROLLER TO\nRUN AROUND A FANTASY WORLD?\n\n \n    \n \n  \n \n\n  \n\nWHAT IF IT WAS\nTHE SAME THING,\nBUT YOU HAD\nTO STAND?\n\n \n     \n \n\n \n\n \n\nI will never understand the idea of a metaverse.\n\f", "https://www.smbc-comics.com/comic/clouds-3": "DO YOU SEE ANYTHING IN THAT ONE LOOKS TO ME LIKE\n\nTHE CLOUDS? A LONNNNG PATHWAY AND AT\nTHE FAR END THERES A LADY\nWITH A SAD FACE LOOKING\nBACK OVER THE PATH\n\n \n\f", "https://www.smbc-comics.com/comic/reviews": "YOU ARE GREAT AT IT\nT HAVE TO TELL YOU ALL OF\nMY FAVORITE PARTS SO LET\nME PULL UP MY NOTES/\n\n       \n      \n  \n\nLIFE TIP:\n\nYOU CAN TELL.\nHOW BAD YOU ARE\nAT SOMETHING BY\n\nHOW UNFOCUSED\nTHE CONSTRUCTIVE\nCRITICISM IS\n\n \n\nYOU ARE DECENT\n\nTHIS IS REALLY NICE WORK\nOVERALL, BUT I HAVE SOME,\nTHOUGHTS. LIKE HERE\nIN CHAPTER 3...\n\n     \n     \n     \n\n  \n   \n     \n\nYOU KNOW IT WAS AN\nINTERESTING EXPERIENCE.\nREADING THE WORDS\nYOU WROTE.\n\n  \n\n \n\naYOUR BOOK? GOOD? BAD,\nWHAT ARE WE? IS ANY OF\nTHIS EVEN REAL?\n\n \n\f"}


@app.get("/base")
async def root():
    #if item_id == '': pass
    return base


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")