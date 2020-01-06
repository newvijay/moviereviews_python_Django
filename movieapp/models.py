from django.db import models

# Create your models here.
class MovieReview(models.Model):
    moviename=models.CharField(max_length=500)
    movierating=models.DecimalField(decimal_places=1,max_digits=2)
    def __str__(self):
        return self.moviename
