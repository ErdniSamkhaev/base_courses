from django.db import models

# Create your models here.

#Здесь миграции нужны при кождом изменении
class base(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=10000000)

    #здесь миграция не нужна
    def __str__(self):
        return f'{self.name}-{self.rating}%'