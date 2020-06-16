import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')

@app.get('/')
def index():
    return(
        {
            "message": "Welcome to FastAPI Tutorials"
        }
    )

@app.get("/item/{id}")
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("index.html", {"request": request, "id": id})



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
    