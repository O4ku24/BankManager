
from Client import Client
from Bank import Bank
import uvicorn
from database import  engine
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles



app = FastAPI(
    title="TodoList",
    version="0.0.1"
)

""" app.include_router(router)
app.include_router(task_temp_url) """


if __name__ == '__main__':
    Client.metadata.create_all(engine)
    Bank.metadata.create_all(engine)
    print('Start Server')
    uvicorn.run('main:app', port = 8000, host='127.0.0.1', reload=True)
    print('Server Stop')

 