<<<<<<< HEAD
<<<<<<< HEAD
from fastapi import FastAPI, Query
=======
=======
>>>>>>> 453f0f1 (3.3 Работа с заголовками запросов)
<<<<<<< HEAD
from fastapi import FastAPI, Depends, status, HTTPException
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials
>>>>>>> 5bb4ba0 (3.2 Дополнительные типы, асинхронность и параметры Cookie)

from app.models import UserCreate

app = FastAPI()

sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

products_db = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]


@app.get('/product/{product_id}')
async def get_product(product_id: int):
    for product in products_db:
        if product_id == product["product_id"]:
            return product
    raise ValueError("Товар в базе отсутствует")


<<<<<<< HEAD
# Задача 2
@app.get('/products/search')
async def search_product(
        keyword: str = Query(),
        category: str = Query(default=None),
        limit: int = Query(default=10)
    ):
    count = 0
    response = []
    for product in products_db:
        if category:
            if keyword in product["name"] and category == product["category"]:
                response.append(product)
                count += 1
        else:
            if keyword in product["name"]:
                response.append(product)
                count += 1
        if count == limit:
            break
    return response
=======
# Симуляция базы данных в виде списка объектов пользователей
USER_DATA = [
    User(**{"username": "user1", "password": "pass1"}),
    User(**{"username": "user2", "password": "pass2"})
]


def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = get_user_from_db(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials",
                            headers={"WWW-Authenticate": "Basic"})
    return user


def get_user_from_db(username: str):
    for user in USER_DATA:
        if user.username == username:
            return user
    return None


@app.get("/login")
def get_protected_resource(user: User = Depends(authenticate_user)):
    return {"message": "You got my secret, welcome"}
=======
from uuid import uuid4
from itsdangerous import URLSafeSerializer
=======
from typing import Annotated
from fastapi import FastAPI, Header, HTTPException
>>>>>>> c6b2001 (0.4.0 Работа с заголовками запросов)


app = FastAPI()


<<<<<<< HEAD
>>>>>>> e39d55e (0.3.0 Дополнительные типы, асинхронность и параметры Cookie)
<<<<<<< HEAD
>>>>>>> 5bb4ba0 (3.2 Дополнительные типы, асинхронность и параметры Cookie)
=======
=======
@app.get('/headers')
def get_headers(
        user_agent: Annotated[str | None, Header()] = None,
        accept_language: Annotated[str | None, Header()] = None
):
    if not user_agent and not accept_language:
        raise HTTPException(status_code=400, detail='Необходимые заголовки отсутствуют')
    return {
        "User-Agent": user_agent,
        "Accept-Language": accept_language
    }
>>>>>>> c6b2001 (0.4.0 Работа с заголовками запросов)
>>>>>>> 453f0f1 (3.3 Работа с заголовками запросов)
