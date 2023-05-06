from django.db import models


class Resource(models.Model):
    image = models.ImageField(upload_to='pics')
    desc = models.CharField(max_length=300)
    category = models.CharField(max_length=20)
    link = models.CharField(max_length=50)
    
    def __str__(self):
        return self.desc