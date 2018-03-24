from django.db import models

# Create your models here.


class media(models.Model):
    name=models.CharField(max_length=100)
    media=models.CharField(max_length=500)
    category=models.CharField(max_length=250)

    def __str__(self):
        return str(self.id)+' '+str(self.name)+' '+str(self.media)+' '+str(self.category)
