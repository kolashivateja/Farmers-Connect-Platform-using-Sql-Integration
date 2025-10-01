from django.db import models
from django.contrib.auth.models import User
class product(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    product_name=models.TextField()
    category =models.TextField()
    price=models.DecimalField(max_digits=7, decimal_places=2)
    status=models.TextField(default='Available')
    def __str__(self):
        return self.product_name
class order(models.Model):
    buyer =models.ForeignKey(User ,on_delete=models.CASCADE)
    item=models.ForeignKey(product, on_delete=models.CASCADE)
    status=models.TextField(default='pending')
    