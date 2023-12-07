from django.urls import path
from .views import home, news_details, categories_form


urlpatterns = [
    path('', home, name='home-page'),
    path('news/<int:id>', news_details, name='news-details-page'),
    path('categories/', categories_form, name='categories-form')
]
