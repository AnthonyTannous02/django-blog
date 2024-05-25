from django.db import models
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.caption}"


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null=True)
    excerpt = models.CharField(max_length=250)
    image_name = models.CharField(max_length=20)
    date = models.DateField()
    content = models.TextField()
    slug = models.SlugField(default="", unique=True, max_length=100, blank=True, null=False, db_index=True)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.author}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_tags(self):
        return ", ".join([t.caption for t in self.tags.all()])
    get_tags.short_description = "tags"