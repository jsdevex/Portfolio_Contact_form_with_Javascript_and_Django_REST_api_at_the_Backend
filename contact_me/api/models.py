from django.db import models

# Create your models here.
class ContactForm(models.Model):
  name = models.CharField(max_length=100, null=True)
  email = models.CharField(max_length=100, null=True)
  message = models.CharField(max_length=1000, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  
  def __str__(self):
    return self.name