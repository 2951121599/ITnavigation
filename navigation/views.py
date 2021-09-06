from django.http import HttpResponse
from django.shortcuts import render
from .models import PartChoice, GroupChoice, Site


def index(request):
    all_part = PartChoice.objects.all()
    all_group = GroupChoice.objects.all()
    all_site = Site.objects.all()
    return render(request, 'navigation/index.html', locals())


def pm(request):
    return render(request, 'navigation/pm.html', locals())


def ui(request):
    return render(request, 'navigation/ui.html', locals())


def cehua(request):
    return render(request, 'navigation/cehua.html', locals())


def blog(request):
    return render(request, 'navigation/blog.html', locals())
