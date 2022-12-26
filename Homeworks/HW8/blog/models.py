from django.db import models

# Create your models here.

class Post(models.Model):
    # define class post that will be edited in the admin page
    title = models.CharField(max_length=300)
    content = models.TextField()
    author_name =  models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
