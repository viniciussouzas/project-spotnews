from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import News

# Create your views here.

def home(request):
    context = {'news': News.objects.all()}
    return render(request, 'home.html', context)


def news_details(request, id):
    context = {'new': get_object_or_404(News, pk=id)}
    return render(request, 'news_details.html', context)
