from django.urls import path
from .views import  courses_list, home


app_name='view'
urlpatterns = [path('', home, name='home'),
               path('courses_list', courses_list, name='courses_list'),
               ]
