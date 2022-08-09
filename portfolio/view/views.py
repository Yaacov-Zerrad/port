from django.shortcuts import get_object_or_404, render
from core.settings import NAME_SITE

from view.models import ExampleModel, IndexPageModel, ServiceModel
from sms import send_sms

# send_sms(
#     'Here is the message',
#     '+12065550100',
#     ['+441134960000'],
#     fail_silently=False
# )

def home(request):
    services =  ServiceModel.objects.all()
    text_page = IndexPageModel.objects.filter(default=True)
    examples = ExampleModel.objects.all()
    
    if text_page:
        text_page = text_page[0]
    return render(request, 'index.html', {'home': True, 'examples':examples, 'services':services, 'text_page':text_page, 'NAME_SITE':NAME_SITE})



def courses(request):
    send_sms(
    'Here is the message',
    '+972586672054',
    ['+972586672054'],
    fail_silently=False
)
    return render(request, 'courses.html')

def examples(request):
    examples = ExampleModel.objects.all()
    return render(request, 'examples.html', {'examples':examples})

def services(request):
    services =  ServiceModel.objects.all()
    return render(request, 'services.html', {'services':services})


def service_detail(request, pk):
    detail = get_object_or_404(ServiceModel, pk=pk)
    return render(request, 'service_detail.html', {'detail':detail})