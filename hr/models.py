from django.db import models


# Create your models here.

class CompanyInfo:
    title = "ABC Ltd."
    email = "abc@gmail.com"
    contact = "9900990099"


# DB Model
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.id},{self.title},{self.author},{self.price}"
