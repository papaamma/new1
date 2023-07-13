from django.db import models

# Create your models here.
class place(models.Model):

    imag=models.ImageField(upload_to='pic')
    desc=models.TextField()
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name
class freedom (models.Model):

    img=models.ImageField(upload_to='pic')
    des=models.TextField()
    nam=models.CharField(max_length=250)
    def __str__(self):
        return self.name





