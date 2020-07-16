from django.db import models

# Create your models here.
# class Dojo(models.Model):
#     name = models.CharField(max_length=50)
#     city = models.CharField(max_lenth=50)
#     state = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Ninja(models.Model):
#     dojo = models.ForeignKey(Dojo, related_name='ninjas', on_delete= models.CASCADE)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)