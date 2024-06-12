from ninja import Schema
from datetime import datetime

class PostSchema(Schema):
    id: int  
    title: str
    content: str
    date: datetime
    image: str 
    votes: int
    
