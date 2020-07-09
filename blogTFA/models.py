from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    FASHION = 'Fashion'
    LIFESTYLE = 'Lifestyle'
    NEWS = 'News'

    DRAFT = 'DRAFT'
    PUBLISHED = 'PUBLISHED'

    SECTIONS = [
       (FASHION, ('Fashion')),
       (LIFESTYLE, ('Lifestyle')),
       (NEWS, ('News')),
    ]

    STATUS_CHOICES = (
    (DRAFT, 'Draft'),
    (PUBLISHED, 'Published'),)


    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_content = models.TextField()
    photo_url = models.CharField(max_length=512)
    post_timestamp = models.DateTimeField(auto_now_add=True)
    section_name = models.CharField(
       max_length=32,
       choices=SECTIONS,
       default=FASHION,
    )
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES,
                                                      default ='draft')
    slug = models.SlugField(max_length=255, null = True, blank = True, unique=True)

    def __str__(self):
        return self.title + " by " + str(self.author)

    class Meta:
       ordering = ('-post_timestamp', )
