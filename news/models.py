from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ('id',)


class Post(models.Model):
    title = models.CharField(max_length=70)
    content=models.TextField()
    category_id = models.ForeignKey(
        Category,related_name= 'blog_posts',on_delete=models.CASCADE
    )
    status = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True,null=True,upload_to='newsImages')

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        ordering = ('id',)