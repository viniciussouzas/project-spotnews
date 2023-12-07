from rest_framework import viewsets
from news.models import Category
from news_rest.serializers.category_serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
