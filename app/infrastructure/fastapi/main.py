from fastapi import FastAPI
from app.infrastructure.database.orm import db, UserModel
from app.controller.user import signup

def create_app():
    app = FastAPI()
    app.add_api_route(
        path="/user",
        methods=['POST'],
        endpoint=signup,
    )
    db.connect()
    UserModel.create_table()
    return app

app = create_app()

# 실행 스크립트
# python -m uvicorn app.infrastructure.fastapi.main:app --port 8000 --reload
