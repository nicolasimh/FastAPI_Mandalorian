# una vez instalado Python
# pip install fastapi
# pip install uvicorn
# uvicorn main:app --reload
# pip install --upgrade pip
# python -m pip freeze > requirements.txt
# pip install --upgrade pip && pip install -r requirements.txt
# uvicorn main:app --host 0.0.0.0 --port 10000
#
import uvicorn
from fastapi import FastAPI
from routers import usuarios

app = FastAPI()
app.include_router(usuarios.router)


@app.get("/")
async def root():
    return "hola Mandalorian"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
