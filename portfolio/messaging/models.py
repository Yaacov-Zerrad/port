import email
from django.db import models
from django.core.validators import RegexValidator
phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    # phone =  models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)

class Contact(models.Model):
    SUBJECT_CHOICES = [
        ('בנית אתרים','בנית אתרים'), 
        ('שיעורים פרטיים','שיעורים פרטיים'), 
        ('דפי מידע','דפי מידע')]
    subject =  models.CharField(
        choices=SUBJECT_CHOICES,
        verbose_name=("בחירת נושא"),
        max_length=255,
    )
    name = models.CharField(max_length=250, verbose_name='שם מלא')
    email = models.EmailField(verbose_name='אמייל')
    title = models.CharField(verbose_name='כותרת',max_length=250)
    message = models.TextField(verbose_name='הודעה')
    phone = models.CharField(verbose_name='פלפון/טלפון', max_length=10, validators = [phoneNumberRegex])
    # img = models.ImageField(verbose_name='קובץ', width_field=200, height_field=150, upload_to='images',blank=True)
    files = models.FileField(verbose_name='קובץ', upload_to='files_contact/',blank=True)

    date_send = models.DateTimeField(auto_now_add=True, blank=True)
    resolved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
        
