from fastapi import FastAPI
from uvicorn import run

from src.app.routes.employee_routes import employee_router
from src.config.config import DEBUG, HOST, PORT

app = FastAPI()

app.include_router(employee_router)

@app.get('/')
async def root():
    return {'message': 'API Works.'}

if __name__ == "__main__":
    run('app:app', host=HOST, port=PORT, reload=DEBUG)
