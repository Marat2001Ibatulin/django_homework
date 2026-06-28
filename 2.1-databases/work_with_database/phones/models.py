from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    name = models.TextField(max_length=30)
    price = models.FloatField(max_length=10)
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
