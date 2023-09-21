import datetime
from django.conf import settings
from django.db import models

# Create your models here.
class TodoItem(models.Model):
    titel = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                               on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.date.today)
    field_name = models.BooleanField(default=False)
    
    def __str__(self):
        return f' ({self.id}) {self.titel} '
    