from django.db import models

# Create your models here.
class Lab(models.Model):
    homesampling = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    )

    Labname = models.CharField(max_length=200, default='')
    # img = models.ImageField(upload_to='lablogo/', default='')
    # email = models.EmailField(default='')
    # password = models.CharField(max_length=100, default='')
    Address = models.TextField(max_length=300, default="")
    Home_Sample = models.CharField(max_length=200, null=True, choices=homesampling, default='Available')

    def __str__(self):
        return self.Labname

