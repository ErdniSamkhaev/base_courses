from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

#Здесь миграции нужны при кождом изменении
class base(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=10000000)
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(base, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('course_detail', args=[self.slug])

    #здесь миграция не нужна
    def __str__(self):
        return f'{self.name}-{self.rating}%'