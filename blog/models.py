from django.db import models

# Create your models here.
# title
# pub_date
# body

class Blog(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')