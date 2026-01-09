from django.db import models
from datetime import date
class smsadmin(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phonenumber = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    img=models.ImageField(upload_to='image',default='')
    password = models.CharField(max_length=50)
    

    def _str_(self): 
        return self.name
class smscategory(models.Model):
    categoryname = models.CharField(max_length=50)
    def _str_(self): 
        return self.categoryname
    
class smssubcategory(models.Model):
    categoryname = models.CharField(max_length=50 ,default='')
    subcategoryname = models.CharField(max_length=50)
    def _str_(self): 
        return self.subcategoryname   
      
class smsproduct (models.Model):
    productname= models.CharField(max_length=50)
    category= models.CharField(max_length=50)      
    subcategory=models.CharField(max_length=50)
    mrp=models.CharField(max_length=50)
    hsn=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    brand=models.CharField(max_length=50)
    warrenty=models.CharField(max_length=50)
    expiry=models.CharField(max_length=50)
    image=models.ImageField(upload_to='image')
    description=models.CharField(max_length=50)
    def str(self): 
        return self.productname

class smscustomer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phonenumber = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    def str(self): 
        return self.name  
    
class smsaccounts(models.Model):
    status = models.CharField(max_length=50)
    billno = models.EmailField(max_length=50)
    customerid = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    date=models.DateTimeField(default=date.today)
    def str(self): 
        return self.status  
class smstemppurchase(models.Model):
    billno = models.EmailField(max_length=50)
    productname = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    def str(self): 
        return self.billno     
class smsfinalpurchase(models.Model):
    billno = models.CharField(max_length=50)
    productname = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    def str(self): 
        return self.billno
    
class stock(models.Model):
    productname = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    def str(self): 
        return self.productname
class smstempsale(models.Model):
    billno = models.EmailField(max_length=50)
    productname = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    def str(self): 
        return self.billno     
class smsfinalsale(models.Model):
    billno = models.CharField(max_length=50)
    productname = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    def str(self): 
        return self.billno

# Create your models here.
    