from rest_framework import serializers
from .models import *

class ProductsSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()
    date = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = TblProduct
        fields = '__all__'
    
    def get_category(self, obj):
        cat = TblProductCategory.objects.get(id=obj.category.id)
        return cat.name

class UsersSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = TblUsers
        fields = '__all__'

class StorageSerializer(serializers.ModelSerializer):
    name_retailer = serializers.SerializerMethodField()
    distance = serializers.SerializerMethodField()
    class Meta:
        model = TblStorage
        fields = '__all__'

    def get_name_retailer(self, obj):
        
        user = TblUsers.objects.get(id = obj.user)
        return user.user

    def get_distance(self, obj):
        user = TblUsers.objects.get(id = obj.user)
        return user.distance

class SharingSerializer(serializers.ModelSerializer):
    send_order = serializers.SerializerMethodField()
    name_product = serializers.SerializerMethodField()
    value_product = serializers.SerializerMethodField()
    class Meta:
        model = TblSharing
        fields = '__all__'
    
    def get_send_order(self, obj):
        user = int(self.context['id_user'])

        if user == obj.send_user.id:
            return True
        else:
            return False
    
    def get_name_product(self, obj):
        return obj.product.name
    
    def get_value_product(self, obj):
        return obj.product.value



class ChatSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TblChat
        fields = '__all__'
    
    def get_send_order(self, obj):
        user = int(self.context['id_user'])

        if user == obj.send_user.id:
            return True
        else:
            return False

class GeolocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TblGeolocation
        fields = '__all__'