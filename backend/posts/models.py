from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    date = models.DateField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def vote(self):
        self.votes += 1
        self.save()
