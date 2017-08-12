from rest_framework import serializers
from .models import *

class ProductsSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()
    date = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = TblProduct
        fields = '__all__'
    
    def get_category(self, obj):
        cat = TblProductCategory.objects.get(id=1)
        return cat.name

class UsersSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = TblUsers
        fields = '__all__'

class StorageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TblStorage
        fields = '__all__'

class SharingSerializer(serializers.ModelSerializer):
    send_order = serializers.SerializerMethodField()

    class Meta:
        model = TblSharing
        fields = '__all__'
    
    def get_send_order(self, obj):
        user = int(self.context['id_user'])

        if user == obj.send_user.id:
            return True
        else:
            return False

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