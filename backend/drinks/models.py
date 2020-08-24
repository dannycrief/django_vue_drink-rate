from django.db import models


class Drink(models.Model):
    name = models.CharField('name', max_length=128)
    description = models.TextField('description', null=True)
    rating = models.IntegerField()

    def __str__(self):
        return '{}. {} '.format(self.id, self.name)
