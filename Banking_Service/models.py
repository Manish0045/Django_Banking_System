from pyexpat import model
from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    avail_bal = models.IntegerField()
    
    def __str__(self):
        return self.name

class transactiondetail(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    deb_amt = models.IntegerField()
    cr_amt = models.IntegerField()
    ac_bal = models.IntegerField()
    
    def __str__(self):
        return self.name,self.ac_bal