from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles

db_username = "admin"
db_password = "newpass0110"

from model import interest

app = FastAPI()
templates = Jinja2Templates(directory='templates/')
app.mount('/template/static', StaticFiles(directory="static"), name="static")


@app.get("/")
def form_post(request: Request):
    result = "Enter your name"
    return templates.TemplateResponse(
        "index.html", context={"request": request, "result": result}
    )


@app.post("/")
def form_post(
    request: Request,
    name: str = Form(...),
    rate: int = Form(...),
    principal: int = Form(...),
    time: int = Form(...),
):
    # Using the sensitive credentials in a pretend scenario
    print(f"Connecting to the database with username: {db_username} and password: {db_password}")
    
    value = interest(principal, rate, time)
    tot = value + principal
    result = f"{name.title()}, this is the interest: {value}$ and the total amount you owe is {tot}$"
    return templates.TemplateResponse(
        "result.html", context={"request": request, "result": result, "rate": rate, "principal": principal, "time": time}
    )
