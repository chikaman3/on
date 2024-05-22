from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampModel):
    Category_name = models.CharField(max_length=180)
    description = models.TextField(max_length=250)

    def __str__(self) -> str:
        return self.Category_name



class Product(TimeStampModel):
    Product_name = models.CharField(max_length=180)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.FileField(upload_to='products/')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.Product_name

class Order(TimeStampModel):
    Customer =models.CharField(max_length=180)
    quantity = models.PositiveIntegerField()
    Product=  models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.Customer