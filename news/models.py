from django.db import models

# Create your models here.
class Category(models.Model):
    # id = models.BigIntegerField()
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    id=models.ForeignKey(
        Category,related_name= 'news',on_delete=models.CASCADE
    )
    title = models.CharField(max_length=70)
    content=models.TextField()
    category_id = models.BigIntegerField()
    status = models.BooleanField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True,null=True,upload_to='newsImages')

    def __str__(self) -> str:
        return f'{self.image}--{self.title}'