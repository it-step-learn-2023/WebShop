from django.db import models

# Create your models here.
class Category(models.Model):
    # Props
    name = models.CharField(max_length=100, unique=True)
    
    # Presintation
    def __str__(self) -> str:
        return str(self.name)
    
class Producer(models.Model):
    # Props
    name = models.CharField(max_length=100, unique=True)
    
    # Presintation
    def __str__(self) -> str:
        return str(self.name)
    
class Product(models.Model):
    # Props
    name = models.CharField(max_length=100, unique=True)
    about = models.TextField(max_length=500, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    photo = models.FileField(upload_to='products/')
    price = models.FloatField()
    
    # Presintation
    def __str__(self) -> str:
        return str(self.name)
    
