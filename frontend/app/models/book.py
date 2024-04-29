from pydantic import BaseModel

from app.models.genre import Genre


class Book(BaseModel):
    title: str
    author: str
    rating: float
    genre: Genre
    cover_image_url: str
    description: str = "Some long long long "