from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib import auth
from multiselectfield import MultiSelectField
from django.utils import timezone
from datetime import datetime
# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=100,default='')
    poster = models.ImageField(upload_to = 'movie_posters',blank=True)
    description = models.CharField(max_length=1000,default='')
    rating = models.FloatField(default=4.5)
    basic_price = models.IntegerField(default=100)
    offer = models.BooleanField(default=False)
    offer_description = models.CharField(max_length=2000,default='',blank=True)
    language_CHOICES = [
    ('Suitcase', 'Suitcase'),
    ('Straws', 'Straws'),
    ('Plates', 'Plates'),
      ('Pen', 'Pen'),
    ('Towel', 'Towel'),
    ('Brush', 'Brush'),

   
    ]
    column_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
   
    ]
    


    Type = models.CharField(choices = language_CHOICES,max_length=100, default='')
    column_number = models.CharField(choices = column_CHOICES,max_length=100, default='')

   
    def __str__(self):
        return self.name






class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #add_any additional
    Location = models.CharField(max_length=100,default='')
    balance = models.IntegerField(default=1500)
    age = models.IntegerField(default='')
    mobilenumber = models.IntegerField(default='')
    cu_CHOICES = [
    ('Public Sector', 'Public Sector'),
    ('Private Sector', 'Private Sector'),
    ('Self-Employed', 'Self-Employed'),
    ('Unemployed', 'UnEmployed'),
    ('Student', 'Student'),
    ]
    occupation = models.CharField(choices = cu_CHOICES,max_length=100, default='M')
    hq_CHOICES = [
    ('Pre-University', 'Pre-University'),
    ('Graduates Degree', 'Graduates Degree'),
    ('Masters Degree ', 'Masters Degree'),
    ('PhD', 'PhD'),
    ('Others', 'Others'),
    ]
    hq = models.CharField(choices = hq_CHOICES,max_length=100, default='M')

    gender_CHOICES = [
    ('M', 'M'),
    ('F', 'F'),
    ]
    
    gender = models.CharField(choices = gender_CHOICES,max_length=100, default='M')
    
    column_CHOICES = [
    ('Below 5 Lakh', 'Below 5 Lakh'),
    ('5-10 Lakh', '5-10 Lakh'),
    ('more than 10 lakh', 'more than 10 lakh'),
   
    ]
    income = models.CharField(choices = column_CHOICES,max_length=100, default='')
 


    def __str__(self):
        return self.user.username

class Ticket(models.Model):
    movie = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.CharField(max_length=100,null=False)
    income = models.CharField(max_length=100,null=True)
    age = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=100,null=True)
    hq = models.CharField(max_length=100,null=True)
    occupation = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=100,null=True)
    post_date = models.DateTimeField(default=datetime.now)



    def __str__(self):
        return self.movie.name + " - " + self.user +"-" +self.age +" - " +self.gender + " -" + self.movie.column_number
    





class Payment(models.Model):
    
    user = models.CharField(max_length=100,null=False)
    card_number = models.IntegerField(default='')
    cvv = models.IntegerField(default='')
    CardHolder_name =  models.CharField(max_length=100)

    def __str__(self):
        return self.user + " "  + " " + self.CardHolder_name