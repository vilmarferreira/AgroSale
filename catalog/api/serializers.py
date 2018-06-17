from rest_framework.serializers import ModelSerializer
from catalog.models import Product,Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields =('id','name')

class ProductSerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'description', 'price', 'category')


