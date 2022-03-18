from apps.products.models import Product

from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('state', 'modified_date', 'created_date', 'deleted_date')
