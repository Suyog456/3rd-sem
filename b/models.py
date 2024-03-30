from django.db import models
from django.conf import settings 
from datetime import date 

# Create your models here.
class product_models(models.Model):
    product_name = models.CharField(max_length = 20)
    price = models.IntegerField()
    description = models.TextField()
    token = models.CharField(max_length = 10 , primary_key = True)
    views = models.IntegerField()
    business_name = models.Foreignkey()
    likes = models.IntegerField()
    picture = models.ImageField()
    category = models.CharField(max_length = 20)
    sub_category = models.CharField(max_length = 20)
    weight = models.IntegerField()
    size = models.CharField()
    negotiable = models.BooleanField()
   # varients = models.ForeignKey()#list of productid
    #comments = models. list of comment id 
class comments(models.Model):
    comment_id = models.CharField(max_length = 10)
    user = models.CharField(max_length = 10)
    product_id = models.CharField(max_length = 10)
    comment = models.TextField()
class ratings(models.Model):
    user = models.CharField(max_length = 10)
    product_id = models.CharField(max_length = 10)
    ratings = models.IntegerField(max_length = 1)
class User_model(models.Model):
    name = models.CharField(max_length = 100 )
    password = models.CharField(max_length = 20)
    email = models.CharField(max_length = 10)
    registered = models.BooleanField(default = 0)
    token = models.CharField(max_length = 10 , primary_key = True)
    ratings = models.ForeignKey(ratings , on_delete = models.CASCADE)
    comments = models.ForeignKey(comments , on_delete = models.CASCADE)
    
class Business_model(models.Model):
    name = models.CharField(max_length = 100)
    contacts = models.IntegerField(max_length = 10)
    description = models.TextField()
    token = models.CharField(max_length = 10 , primary_key = True)
    products = models.ForeignKey(product_models , on_delete = models.CASCADE)
    #interaction = models.ForeignKey(interactions , on_delete = models.CASCADE)
    views = models.IntegerField()



    
    