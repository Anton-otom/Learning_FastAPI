from typing import Annotated
from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: Annotated[int, Field(gt=0)] = None
    is_subscribed: bool = None


if __name__ == "__main__":
    pass
