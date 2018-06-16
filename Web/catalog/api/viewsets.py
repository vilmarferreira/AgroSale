from rest_framework.viewsets import ModelViewSet
from catalog.models import Product,Category
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



