from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name
    
    
