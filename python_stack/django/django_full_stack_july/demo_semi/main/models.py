from django.db import models
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

class ShowManager(models.Model):
    def show_validator(self, post_data):
        errors = {}
        if len(post_data['title']) < 2:
            errors['title'] = "Your title must be longer than 2 characters!"
        if len(post_data['release_date']) == 0:
            errors['release_date'] = "You gotta add something"
        if len(post_data['description']) < 8:
            errors['description'] = "Put something longer"

        return errors
    
class User(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Network(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Show(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.CharField(max_length=50)
    submitted_by = models.ForeignKey(User, related_name='shows0', on_delete=models.CASCADE)
    network = models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
