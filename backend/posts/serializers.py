from ninja import Schema
from datetime import datetime

class PostSchema(Schema):
    title: str
    content: str
    date: datetime
    image: str  # This will be the URL of the uploaded image
