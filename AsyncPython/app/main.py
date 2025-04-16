from app.config import load_config
from fastapi import FastAPI

from app.models import User


app = FastAPI()

# config = load_config()
#
# if config.debug:
#     app.debug = True
# else:
#     app.debug = False

data = {"name": "John Doe", "age": 25}
user1 = User(**data)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/users")
def get_users():
    return user1


@app.post("/user")
def post_user_age(user: User):
    if user.age >= 18:
        user.is_adult = True
    return user

