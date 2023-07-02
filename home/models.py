from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__ (self):
        return self.name
class Blog(models.Model):
    title = models.TextField()
    body = models.TextField()
    full_body = models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    date = models.DateField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=50)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
