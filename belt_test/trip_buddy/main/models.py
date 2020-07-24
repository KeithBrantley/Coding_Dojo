from django.db import models
from datetime import datetime, date, time
from django.utils.dateparse import parse_date
import re, bcrypt

# Create your models here.

class UserManager(models.Manager):
    def registration_validator(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 3:
            errors['first_name'] = 'You must have 3 characters in your name!'
        if len(post_data['last_name']) < 3:
            errors['last_name'] = 'You must have 3 characters in your name!'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):           
            errors['email'] = "Invalid email address!"
        if post_data['password'] != post_data['confirm_pw']:
            errors['confirm_pw'] = 'Passwords do not match!'
        return errors

    def login_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['login_email']):           
            errors['login_email'] = "Email isn't in the Database!"

        return errors

class TripManager(models.Manager):
    def trip_validator(self, postData):
        errors = {}
        if len(postData['destination']) == '':
            errors['destination'] = "You must not leave this field empty!"
        if len(postData['destination']) < 3:
            errors['destination'] = "Destination must be longer than 3 characters"
        if len(postData['start_date']) == 0:
            errors['start_date'] = "Add a start date!"
        if len(postData['end_date']) == 0:
            errors['end_date'] = "Add an end date!"
        if len(postData['plan']) == 0:
            errors['plan'] = "What's your plan!?"
        if len(postData['plan']) < 2:
            errors['plan'] = "Really? That's all your going to do?!"

        return errors

    def edit_validator(self, postData):
        errors = {}
        if len(postData['destination']) < 3:
            errors['destination'] = "You destination needs more than 3 characters"
        if len(postData['plan']) < 3:
            errors['plan'] = "You plan needs more than 3 characters"
        if not postData['start_date']:
            errors['start_date'] = "Add an updated start date"
        if not postData['end_date']:
            errors['end_date'] = "Add an updated end date"

        return errors
        
class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    plan = models.TextField()
    user = models.ForeignKey(User, related_name="trips", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()

