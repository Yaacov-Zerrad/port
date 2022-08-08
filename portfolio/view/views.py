from django.shortcuts import get_object_or_404, render
from core.settings import NAME_SITE

from view.models import IndexPageModel, ServiceModel


def home(request):
    services =  ServiceModel.objects.all()
    text_page = IndexPageModel.objects.filter(default=True)
    text_page = text_page[0]
    return render(request, 'index.html', {'home': True, 'services':services, 'text_page':text_page, 'NAME_SITE':NAME_SITE})



def courses(request):
    return render(request, 'courses.html')

def examples(request):
    return render(request, 'examples.html')

def services(request):
    services =  ServiceModel.objects.all()
    return render(request, 'services.html', {'services':services})


def service_detail(request, pk):
    detail = get_object_or_404(ServiceModel, pk=pk)
    return render(request, 'service_detail.html', {'detail':detail})