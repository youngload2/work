from rest_framework import serializers
from .models import Coa, Product

class CoaSerializer(serializers.ModelSerializer):
    # coa = serializers.HyperlinkedIdentityField(view_name='coa-list')

    class Meta:
        model = Coa
        #exclude = ['id']
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'