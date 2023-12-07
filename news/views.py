from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import News, Category
from .forms import CreateCategoryForm

# Create your views here.

def home(request):
    context = {'news': News.objects.all()}
    return render(request, 'home.html', context)


def news_details(request, id):
    context = {'new': get_object_or_404(News, pk=id)}
    return render(request, 'news_details.html', context)


def categories_form(request):
    form = CreateCategoryForm()

    if request.method == "POST":
        form = CreateCategoryForm(request.POST)

        Category.objects.create(name=form.data['name'])
        return redirect("home-page")
    context = {'form': form}
    return render(request, 'categories_form.html', context)