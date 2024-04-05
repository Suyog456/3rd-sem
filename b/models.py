from django.db import models
from django.conf import settings 
from datetime import date ,datetime,time
import schedule
# Create your models here.
class product_models(models.Model):
    product_name = models.CharField(max_length = 20)
    price = models.IntegerField()
    description = models.TextField()
    token = models.CharField(max_length = 10 , primary_key = True)
    views = models.IntegerField()
    #business_name = models.Foreignkey()
    likes = models.IntegerField()
    picture = models.ImageField()
    category = models.CharField(max_length = 20)
    sub_category = models.CharField(max_length = 20)
    weight = models.IntegerField()
    size = models.CharField(max_length = 10)
    negotiable = models.BooleanField()
   # varients = models.Foreignkey()#list of productid
    #comments = models. list of comment id 
class comments(models.Model):
    comment_token = models.CharField(max_length = 10)
    user = models.ForeignKey(user_model , on_delete = models.CASCADE)
    product_id = models.ForeignKey(product_models , on_delete = models.CASCADE)
    comment = models.TextField()
    business = models.ForeignKey(Business_model , on_delete = models.CASCADE)
class ratings(models.Model):
    user = models.ForeignKey(user_model , on_delete = model.CASCADE)
    product_id = models.ForeignKey(product_models , on_delete = model.CASCADE)
    ratings = models.IntegerField()
    
class user_model(models.Model):
    name = models.CharField(max_length = 100 )
    password = models.CharField(max_length = 20)
    email = models.CharField(max_length = 10)
    registered = models.BooleanField(default = 0)
    token = models.CharField(max_length = 10 , primary_key = True)
    ratings = models.IntegerField()
    comments = models.IntegerField()
    
class business_model(models.Model):
    name = models.CharField(max_length = 100)
    contacts = models.IntegerField()
    description = models.TextField()
    token = models.CharField(max_length = 10 , primary_key = True)
    #interaction = models.Foreignkey(interactions , on_delete = models.CASCADE)
    
    reviews = models.IntegerField()
    avg_rating = models.IntegerField()
    today_views = models.IntegerField()
    monthly_views = models.IntegerField()
    views_record = models.TextField()
    def auto_update(self):
        now = datetime.now()
        hour = now.hour
        if hour == 0:
            self.monthly_views += self.today_views
            self.today_views = 0
        
            self.save()
    schedule.every().hour.do(auto_update)
    
def category_saver(models.Model):
    category = models.CharField(max_length = 30)
    subcategory = models.TextField()
def update_business_models_at_midnight():
    now = datetime.now()
    # Check if it's 12 PM (noon)
    if now.time() == time(12, 0):
        # Call auto_update for all business models
        for model in business_model.objects.all():
            model.auto_update()
    
    