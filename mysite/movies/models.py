from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.DurationField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    genre = models.CharField(max_length=100, default='Romantic')
    image = models.ImageField(upload_to='movies/', blank=True, null=True, default='movies/default.jpg')

    def __str__(self):
        return self.title
