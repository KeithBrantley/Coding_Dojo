from django.db import models
from django.utils import timezone, timedelta
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

class MessageManager(models.Manager):
    def message_validator(self, post_data):
        errors = {}
        timeLimit = timezone.now() - timedelta(minutes = 30)
        if Message.objects.filter(id = post_data['messageId'])[0].created_at < timeLimit:
            errors[post_data['messageId']] = "Cannot delete the Comment anymore! Remember you only have 30mins to delete the post before it becomes permenant"
            print(f"Error message created: {post_data['messageId']}")
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class Comment(models.Model):
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comment", on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
