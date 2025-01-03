from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles

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


@app.post('/')
def form_post(request: Request, name: str = Form(...), rate: int = Form(...),  principal: int = Form(...),  time: int = Form(...)):
    value = interest(principal, rate, time)
    tot = value + principal
    result = f"{name.title()}, this is the interest: {value}$ and the total amount you owe is {tot}$"
    return templates.TemplateResponse('result.html', context={"request": request, 'result': result, 'rate': rate, 'principal': principal, 'time': time})



# Example 1: Inefficient use of loops
def inefficient_loop():
    large_list = [i for i in range(10000)]
    total = 0
    for i in large_list:
        for j in large_list:
            total += i * j  # Nested loop causing inefficiency
    print(f"Total: {total}")

# Example 2: Hardcoded credentials (Security Issue)
def use_hardcoded_credentials():
    username = "admin"
    password = "123456"  # Sensitive data hardcoded
    print(f"Logging in with {username} and {password}")

# Example 3: Unused variable
def unused_variable():
    x = 10  # Variable is declared but never used
    print("This function has an unused variable.")

# Example 4: Deprecated library usage
import random
def deprecated_library_usage():
    data = [1, 2, 3, 4, 5]
    random.shuffle(data)  # Potentially inefficient randomization
    print(f"Shuffled data: {data}")

# Call the functions
inefficient_loop()
use_hardcoded_credentials()
unused_variable()
deprecated_library_usage()
