from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from github_repo.read_git_repo_status import check_commits_today
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Root route to serve the index.html
@app.get("/")
async def read_item(request: Request):
    check_commits_today()
    return templates.TemplateResponse(
        request=request, name="index.html", context={"done": check_commits_today()}
    )
