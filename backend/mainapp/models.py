from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class BasePost(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    description = models.TextField(_('Description'), blank=True, null=True)
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
        verbose_name_plural = _('Elonlar')


class Yangiliklar(BasePost):
    class Meta:
        verbose_name_plural = _('Yangiliklar')

class Yunalishlar(models.Model):
    title = models.CharField(_('Title'), max_length=20, null=False, blank=False)
    description = models.TextField(_('Description'), max_length=100, null=True, blank=True)
    icon = models.ImageField(upload_to='yunalishlar/icons/', blank=True, null=True)
    image = models.ImageField(upload_to='yunalishlar/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _("Yunalishlar")   






class GalleryImage(models.Model):

    
    elonlar = models.ForeignKey(
        'Elonlar', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name='gallery'
    )
    
    yangiliklar = models.ForeignKey(
        'Yangiliklar', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name='gallery'
    )
    
    image = models.ImageField(upload_to='galleries/')
    caption = models.CharField(max_length=255, blank=True)
    
    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
        
    def __str__(self):
        return f"Image for post ID {self.elonlar.id if self.elonlar else self.yangiliklar.id}"