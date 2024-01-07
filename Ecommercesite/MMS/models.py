from django.db import models

# Create your models here.

# Model representing products in the system
class products(models.Model):
    # Field for the title of the product
    Title = models.CharField(max_length=200)

    # Field for the price of the product
    Price = models.FloatField()

    # Field for the discount applied to the product
    Discount = models.FloatField()

    # Field for the category of the product
    Category = models.CharField(max_length=200)

    # Field for the description of the product
    Description = models.TextField()

    # Field for the image URL or path of the product
    Image = models.CharField(max_length=300)
