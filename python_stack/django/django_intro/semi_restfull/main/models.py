from django.db import models

# Create your models here.

class ShowManager(models.Manager):
    def validator(self, post_data):
        errors = {}
        if len(post_data['title']) < 2:
            errors['title'] = 'Title has to be atleast 3 characters long'
        if len(post_data['network']) < 3:
            errors['network'] = 'Network has to be atleast 3 characters long'
        if len(post_data['description']) < 10:
            errors['description'] = 'Description has to be atleast 10 characters long'
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
