from django.db import models

# Create your models here.

class Cost(models.Model):
    From_city=models.CharField(max_length=250)
    To_city=models.CharField(max_length=250)
    Price=models.CharField(max_length=6)
    J_ID=models.CharField(max_length=6)

    def __str__(self):
        return str(self.id)+' '+str(self.From_city)+' '+str(self.To_city)+' '+str(self.Price)+' '+str(self.J_ID)
