from django.db import models
from django.utils.text import slugify

class BasePost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['-date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Elonlar(BasePost):
    class Meta:
        verbose_name_plural = 'Elonlar'


class Yangiliklar(BasePost):
    class Meta:
        verbose_name_plural = 'Yangiliklar'