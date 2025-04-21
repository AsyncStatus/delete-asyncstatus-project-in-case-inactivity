from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Mount the static directory
app.mount("/static", StaticFiles(directory="templates"), name="static")

# Root route to serve the index.html
@app.get("/")
async def read_root():
    return FileResponse("templates/index.html")