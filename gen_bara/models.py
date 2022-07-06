from django.db import models



class Bara(models.Model):
    bara = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    art = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.bara}\n{self.name}\n{self.art}'
