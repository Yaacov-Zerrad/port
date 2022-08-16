from django.shortcuts import get_object_or_404, render
from core.settings import NAME_SITE

from view.models import ExampleModel, IndexPageModel, SatisticModel, ServiceModel
# satistic = SatisticModel.objects.get_or_create(id=1)
def site_view():
    satistic, created = SatisticModel.objects.get_or_create(id=1)
    if created == False:
        satistic.home_view+=1
        satistic.home_view_week+=1
        satistic.save()
        
        
def home(request):
    site_view()
    services =  ServiceModel.objects.all()
    text_page = IndexPageModel.objects.filter(default=True)
    examples = ExampleModel.objects.all()
    
    if text_page:
        text_page = text_page[0]
    return render(request, 'index.html', {'home': True, 'examples':examples, 'services':services, 'text_page':text_page, 'NAME_SITE':NAME_SITE})



def courses(request):
    site_view()
    return render(request, 'courses.html')

def examples(request):
    site_view()
    examples = ExampleModel.objects.all()
    return render(request, 'examples.html', {'examples':examples})

def services(request):
    site_view()
    services =  ServiceModel.objects.all()
    return render(request, 'services.html', {'services':services})


def service_detail(request, pk):
    site_view()
    detail = get_object_or_404(ServiceModel, pk=pk)
    return render(request, 'service_detail.html', {'detail':detail})