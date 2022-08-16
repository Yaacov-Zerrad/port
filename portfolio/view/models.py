from time import strftime
from django.db import models

# from django_imgur.storage import ImgurStorage
# STORAGE = ImgurStorage()
# from core.settings import STORAGE_MEDIA
from cloudinary.models import CloudinaryField


class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''



class ServiceModel(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    

    
    def __str__(self):
        return self.title
    
    
class IndexPageModel(models.Model):
    title_masthead = models.CharField(max_length=255)
    description_masthead = models.TextField()
    title_service = models.CharField(max_length=255)
    description_about = models.TextField()
    title_about = models.CharField(max_length=255)
    title_befor_fotter = models.CharField(max_length=255)
    button_befor_fotter = models.CharField(max_length=555)
    
    date_create = CustomDateTimeField(auto_now_add=True, blank=True)
    default = models.BooleanField(default=True)
    
    def default_text(self):
        if self.default == True:
            for obj in self.objects.all():
                obj.default = False
                obj.save()
                
    
    def __str__(self):
        return f'update on: {self.date_create.strftime("%d-%m-%Y %H:%M")}'
    
    def save(self, *args, **kwargs):
        if self.default == True:
            for obj in IndexPageModel.objects.all():
                obj.default = False
                obj.save()
        super(IndexPageModel, self).save(*args, **kwargs)
        
class ExampleModel(models.Model):
    category = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/', height_field="avatar_height", width_field="avatar_width",blank=True)
    # img = CloudinaryField('image')
    slug_auto = models.SlugField(blank=True)
    # slug = models.SlugField(blank=True)
    url = models.CharField(max_length=255, blank=True)
    avatar_height = 650
    avatar_width = 350
        
    def __str__(self):
        return self.project_name
    
    
class SatisticModel(models.Model):
    home_view = models.PositiveIntegerField(default=0)
    home_view_week = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.home_view