from django.db import models

class State(models.Model):
    new_name    = models.CharField(max_length=200)
    new_phone   = models.IntegerField()
    new_email   = models.EmailField()
    
    timestamp           = models.DateTimeField(auto_now_add=True)
