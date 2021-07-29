from django.http import HttpResponse
from django.shortcuts import render
from .models import PartChoice, GroupChoice, Site


def index(request):
    all_part = PartChoice.objects.all()
    all_group = GroupChoice.objects.all()
    all_site = Site.objects.all()
    print("all_part------\n", all_part)
    
    return render(request, 'navigation/index.html', locals())


def pm(request):
    return render(request, 'navigation/product.html', locals())
