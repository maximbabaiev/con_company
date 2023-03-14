from django.shortcuts import render
from about_site.models import *


# Create your views here.

def index(request):
    context = {
        'title': 'Construction company',
        'projects': Project.objects.all()
    }
    return render(request, 'index.html', context)
