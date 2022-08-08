from django.urls import path
from .views import  service_detail, courses, home, examples, services


app_name='view'
urlpatterns = [path('', home, name='home'),
               path('courses', courses, name='courses'),
               path('examples', examples, name='examples'),
               path('services', services, name='services'),
               path('service-detail/<int:pk>', service_detail, name='service-detail')
               ]
