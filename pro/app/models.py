from django.db import models
from django.contrib.auth.models import User
class Watch(models.Model):
    brand=models.CharField(max_length=250)
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    image=models.ImageField(upload_to='gallery')
    color=models.CharField(max_length=200)
    image2=models.ImageField(upload_to='gallery')
    image3=models.ImageField(upload_to='gallery')
    material=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class CartItem(models.Model):
    product = models.ForeignKey(Watch, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
# Create your models here.
    # class Meta:
    #     order_with_respect_to = 'user'