from ninja import Schema
from datetime import datetime

class PostSchema(Schema):
    id: int  # ID 필드 추가
    title: str
    content: str
    date: datetime
    image: str  # 업로드된 이미지의 URL
