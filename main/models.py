from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=50, default='General')
    banner = models.ImageField(default='media/My Snapshot.jpg', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    likes = models.ManyToManyField(User, related_name='liked_post', blank=True)
    is_draft = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    views = models.PositiveIntegerField(default=0)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.author} on {self.post}"