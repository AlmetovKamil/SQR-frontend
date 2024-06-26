from typing import List, Optional, Dict
from pydantic import BaseModel

from app.models.genre import Genre
from app.models.review import Review


class Book(BaseModel):
    id: str
    title: str
    author_name: str = ""
    rating: Optional[float] = None
    genre: Genre = Genre.fiction
    cover_link: str
    description: Optional[str] | Optional[Dict] = None
    reviews: List[Review] = []

    def get_rating(self):
        ratings = [e.rating for e in self.reviews]
        rating = sum(ratings)/len(ratings)
        return rating
