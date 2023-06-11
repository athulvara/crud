from django.db import models

# Create your models here.
class change(models.Model):
    img=models.ImageField(upload_to='pics')

class Form(models.Model):
    num=models.IntegerField()
    name=models.CharField(max_length=250)
    desc=models.TextField()

    def __str__(self):
        return self.name
    