from django.db import models

# Create your models here.


class ShowManager(models.Manager):
    def validator(self, post_data):
        errors = {}
        if len(post_data['title']) < 3:
            errors["title"] = "Enter at least 3 characters for the Title!"
        if len(post_data['network']) < 2:
            errors["network"] = "Enter at least 2 characters for the Network!"
        if len(post_data['description']) < 10:
            errors["description"] = "Enter at least 10 characters for the Description!"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
