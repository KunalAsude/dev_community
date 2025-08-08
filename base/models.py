from django.db import models

class room(models.Model):
    name = models.CharField(max_length=200)
    Description = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

