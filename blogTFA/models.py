from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    FASHION = 'Fashion'
    LIFESTYLE = 'Lifestyle'
    NEWS = 'News'

    SECTIONS = [
       (FASHION, ('Fashion')),
       (LIFESTYLE, ('Lifestyle')),
       (NEWS, ('News')),
   ]


    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    photo_url = models.CharField(max_length=512)
    post_timestamp = models.DateTimeField(auto_now_add=True)
    post_section = models.CharField(
       max_length=32,
       choices=SECTIONS,
       default=FASHION,
    )
    slug = models.SlugField()

    def __str__(self):
        return self.title + " by " + self.author
