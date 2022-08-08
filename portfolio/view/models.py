from django.db import models



class ServiceModel(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    

    
    def __str__(self):
        return self.title
    
    
class IndexPageModel(models.Model):
    title_masthead = models.CharField(max_length=255)
    description_masthead = models.CharField(max_length=555)
    title_service = models.CharField(max_length=255)
    description_about = models.CharField(max_length=555)
    title_about = models.CharField(max_length=255)
    description_about = models.CharField(max_length=555)
    title_befor_fotter = models.CharField(max_length=255)
    button_befor_fotter = models.CharField(max_length=555)
    
    date_create = models.DateTimeField(auto_now=True, blank=True)
    default = models.BooleanField(default=True)
    
    def default_text(self):
        if self.default == True:
            for obj in self.objects.all():
                obj.default = False
                obj.save()
                
    
    def __str__(self):
        return f'create at {self.date_create}'
    
    def save(self, *args, **kwargs):
        if self.default == True:
            for obj in IndexPageModel.objects.all():
                obj.default = False
                obj.save()
        super(IndexPageModel, self).save(*args, **kwargs)