from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

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
    carousel_urls = models.TextField(null = True, blank = True)
    post_timestamp = models.DateTimeField(auto_now_add=True)
    category_name = models.CharField(
       max_length=32,
       choices=SECTIONS,
       default=FASHION,
    )
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES,
                                                      default ='draft')
    slug = models.SlugField(max_length=255, null = True, blank = True, unique=True)


    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = Post.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = Post.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title + " by " + str(self.author)

    class Meta:
       ordering = ('-post_timestamp', )
