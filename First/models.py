from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=122)
    phone = models.PositiveBigIntegerField(max_length=10,validators=[MinLengthValidator(10)])
    date = models.DateField()
        
    def __str__(self):
        return self.name

