from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.utils import translation

class BasePost(models.Model):
    title = models.CharField(_('Title'), max_length=200, null=False, blank=False)
    description = models.TextField(_('Description'), blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=False, null=False)
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

    def get_absolute_url(self):
        return f"/elonlar/{self.slug}/"


class Yangiliklar(BasePost):
    class Meta:
        verbose_name_plural = _('Yangiliklar')

    def get_absolute_url(self):
        return f"/yangiliklar/{self.slug}/"

class Yunalishlar(models.Model):

    KURS = [
        ("9-SINF", "9-SINF"),
        ("11-SINF", "11-SINF"),
    ]

    KURS_RU = [
        ("9-Х КЛАССОВ", "9-Х КЛАССОВ"),
        ("11-Х КЛАССОВ", "11-Х КЛАССОВ"),
    ]

    KURS_EN = [
        ("9TH GRADE", "9TH GRADE"),
        ("11TH GRADE", "11TH GRADE"),
    ]

    SHAKL = [
        ("KUNDUZGI", "KUNDUZGI"),
        ("DUAL", "DUAL"),
    ]

    SHAKL_RU = [
        ("ОЧНУЮ", "ОЧНУЮ"),
        ("ДУАЛЬНУЮ", "ДУАЛЬНУЮ"),
    ]

    SHAKL_EN = [
        ("DAYTIME", "DAYTIME"),
        ("DUAL", "DUAL"),
    ]

    title = models.CharField(_('Title'), max_length=20, null=False, blank=False)
    description = models.TextField(_('Description'), max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='yunalishlar/', blank=False, null=False)
    kurs = models.CharField(_('Kurs UZ'), choices=KURS, default={"9-SINF":"9-SINF"}, null=False, blank=False)
    kurs_ru = models.CharField(_('Kurs RU'), choices=KURS_RU, default={"9-Х КЛАССОВ":"9-Х КЛАССОВ"}, null=False, blank=False)
    kurs_en = models.CharField(_('Kurs EN'), choices=KURS_EN, default={"9TH GRADE":"9TH GRADE"}, null=False, blank=False)
    shakl = models.CharField(_('Shakl UZ'), choices=SHAKL, default={"KUNDUZGI" : "KUNDUZGI"}, null=False, blank=False)
    shakl_ru = models.CharField(_('Shakl RU'), choices=SHAKL_RU, default={"ОЧНУЮ" : "ОЧНУЮ"}, null=False, blank=False)
    shakl_en = models.CharField(_('Shakl EN'), choices=SHAKL_EN, default={"DAYTIME" : "DAYTIME"}, null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _("Yunalishlar")

    @property 
    def current_course(self):
        lang_code = translation.get_language()

        if lang_code == "ru" and self.kurs_ru:
            return self.kurs_ru
        
        elif lang_code == "en" and self.kurs_en:
            return self.kurs_en
        else:
            return self.kurs


    @property
    def current_time(self):
        lang_code = translation.get_language()

        if lang_code == "ru" and self.shakl_ru:
            return self.shakl_ru
        
        elif lang_code == "en" and self.shakl_en:
            return self.shakl_en
        else:
            return self.shakl

    def get_absolute_url(self):
        return f"/yo`nalishlar/{self.slug}/"




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

    haqimizda = models.ForeignKey(
        'Haqimizda',
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
        

class Rahbariyat(models.Model):
    ism_familya = models.CharField(blank=False, null=False)
    sohasi = models.CharField(max_length=100, blank=False, null=False)
    mutaxassis = models.TextField(blank=False, null=False)
    haqida = models.TextField(blank=False, null=False)
    yutuqlar = models.TextField(blank=False, null=False)
    maqsadlarim = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='rahbariyat/', blank=False, null=False)


    class Meta:
        verbose_name_plural = _("Rahbariyat")

    def __str__(self):
        return self.ism_familya

    def get_absolute_url(self):
        return "/rahbariyat/"
    

class Haqimizda(models.Model):
    title = models.CharField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name_plural = _("Biz haqimizda")

    def get_absolute_url(self):
        return "/hamkorlik/"
    
