from django.db import models
from django.urls import reverse
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100, blank=True)
    deadline = models.DateField()
    read = models.BooleanField(default=False)
    past_deadline = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])
# Create your models here.

