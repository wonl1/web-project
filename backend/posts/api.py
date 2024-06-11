from ninja import NinjaAPI, File, Form
from ninja.files import UploadedFile
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSchema
from datetime import datetime
from typing import List

api = NinjaAPI()

@api.post("/upload/", response=PostSchema)
def upload_file(request, title: str = Form(...), description: str = Form(...), dateTaken: str = Form(...), file: UploadedFile = File(...)):
    date_taken = datetime.strptime(dateTaken, '%Y-%m-%d')  # 문자열을 datetime 객체로 변환
    post = Post.objects.create(
        title=title,
        content=description,
        image=file,
        date=date_taken
    )
    return post

@api.get("/posts/{post_id}", response=PostSchema)
def get_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return post

@api.get("/posts/", response=List[PostSchema])
def list_posts(request):
    posts = Post.objects.all()
    return posts

@api.delete("/posts/{post_id}/")
def delete_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return {"success": True}
