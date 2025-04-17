from fastapi import FastAPI, Query

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
