import re

from typing import Annotated
from pydantic import BaseModel, Field, AfterValidator, EmailStr


def check_bad_words(value: str) -> str:
    if re.search(r'\bредиск|\bбяк|\bкозявк', value.lower()):
        raise ValueError('Использование недопустимых слов')
    return value


def check_phone(value: str) -> str:
    if not re.search(r'^[0-9]{7,15}$', value):
        raise ValueError('Ошибка в формате номера')
    return value


class Contact(BaseModel):
    email: EmailStr
    phone: Annotated[str, AfterValidator(check_phone)] = None
    is_premium: bool = False


class Feedback(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=50)]
    message: Annotated[str, Field(min_length=10, max_length=500), AfterValidator(check_bad_words)]
    contact: Contact


if __name__ == "__main__":
    pass
