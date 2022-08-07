from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {'home': True})



def courses_list(request):
    return render(request, 'courses/courses_list.html')