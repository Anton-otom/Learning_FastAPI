from fastapi import FastAPI

from app.models import Feedback

app = FastAPI()

feedback_db = []


@app.get('/messages')
async def get_feedback():
    return feedback_db


# Задача 2
@app.post('/feedback')
async def add_feedback(feedback: Feedback, is_premium: bool = False):
    feedback.contact.is_premium = is_premium
    feedback_db.append(feedback)
    message = f"Спасибо, {feedback.name}! Ваш отзыв сохранён."
    if is_premium:
        message += " Ваш отзыв будет рассмотрен в приоритетном порядке."
    return {"message": message}
