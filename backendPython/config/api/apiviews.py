from rest_framework.views import APIView

from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

from .models import *
from .serializer import *

from django.db.models import Q

class Products (APIView):

    def _get_object (self, key=None, name=None ):
        try:
            if key:
                products = TblProduct.objects.filter(id=key)
            elif name:
                products = TblProduct.objects.filter(name__icontains = name)
            else:
                products = TblProduct.objects.all()
        except:
            raise Http404

        return products

    def get(self, request, format=None):
        key = request.GET.get('key', None)
        name = request.GET.get('name', None)

        try:
            products = self._get_object(key, name)
            products = ProductsSerializer(products, many=True).data
            return Response(products)
        except Exception as e:
            return Response({'error': e, 'server_unavailable': True}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Users (APIView):
    
    def _get_object (self, cpf=None, name=None ):
        try:
            if cpf:
                users = TblUsers.objects.filter(id=cpf)
            elif name:
                users = TblUsers.objects.filter(user__icontains = name)
            else:
                users = TblUsers.objects.all()
        except:
            raise Http404

        return users

    def get(self, request, format=None):
        cpf = request.GET.get('cpf', None)
        name = request.GET.get('name', None)

        try:
            users = self._get_object(cpf, name)
            users = UsersSerializer(users, many=True).data
            return Response(users)
        except Exception as e:
            return Response({'error': e, 'server_unavailable': True}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Storage(APIView):
    
    def _get_object (self, user=None, product=None, name=None ):
        try:
            if user:
                storage = TblStorage.objects.filter(user=user)
            elif product:
                storage = TblStorage.objects.filter(product = product)
            elif name:
                storage = TblStorage.objects.filter(product__name__icontains = name)
            else:
                storage = TblStorage.objects.all()
        except:
            raise Http404

        return storage

    def get(self, request, format=None):
        user = request.GET.get('user', None)
        product = request.GET.get('product', None)
        name = request.GET.get('name', None)

        try:
            storage = self._get_object(user, product, name)
            storage = StorageSerializer(storage, many=True).data
            return Response(storage)
        except Exception as e:
            return Response({'error': e, 'server_unavailable': True}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request, key=None, format=None):
        
        if request.data.get('id'):
            obj = TblStorage.objects.get(id = request.data['id'] )
        
            storage = StorageSerializer(obj, request.data, partial=True)
        else:
            storage = StorageSerializer(data=request.data, partial=True)

        if storage.is_valid():
            storage.save()
            return Response(status.HTTP_200_OK)
        
        return Response(storage.errors, status=status.HTTP_400_BAD_REQUEST)

class Sharing(APIView):
    
    def _get_object (self, user=None ):
        try:
            storage = TblSharing.objects.filter(Q(send_user=user)|Q(receive_user=user))
        except:
            raise Http404

        return storage

    def get(self, request, format=None):
        user = request.GET.get('user', None)

        try:
            sharing = self._get_object(user)
            sharing = SharingSerializer(sharing, many=True, context={'id_user': user}).data
            return Response(sharing)
        except Exception as e:
            return Response({'error': e, 'server_unavailable': True}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request, key=None, format=None):
        
        if request.data.get('id'):
            obj = TblSharing.objects.get(id = request.data['id'] )
        
            sharing = SharingSerializer(obj, request.data, partial=True,context={'id_user': request.data.get('user')})
        else:
            sharing = SharingSerializer(data=request.data, partial=True)

        if sharing.is_valid():
            sharing.save()
            return Response(status.HTTP_200_OK)
        
        return Response(sharing.errors, status=status.HTTP_400_BAD_REQUEST)
        

class Chat(APIView):
    
    def _get_object (self, user=None ):
        try:
            storage = TblChat.objects.filter(Q(send_user=user)|Q(receive_user=user))
        except:
            raise Http404

        return storage

    def get(self, request, format=None):
        user = request.GET.get('user', None)

        try:
            chat = self._get_object(user)
            chat = ChatSerializer(chat, many=True, context={'id_user': user}).data
            return Response(chat)
        except Exception as e:
            return Response({'error': e, 'server_unavailable': True}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request, key=None, format=None):
        
        if request.data.get('id'):
            obj = TblChat.objects.get(id = request.data['id'] )
        
            chat = ChatSerializer(obj, request.data, partial=True,context={'id_user': request.data.get('user')})
        else:
            chat = ChatSerializer(data=request.data, partial=True)

        if chat.is_valid():
            chat.save()
            return Response(status.HTTP_200_OK)
        
        return Response(chat.errors, status=status.HTTP_400_BAD_REQUEST)

class Geolocation(APIView):
    
    def _get_object (self, address=None, name=None ):
        try:
            storage = TblGeolocation.objects.filter(Q(name=name)|Q(address=address))
        except:
            raise Http404

        return storage

    def get(self, request, format=None):
        address = request.GET.get('address', None)
        name = request.GET.get('name', None)
        try:
            geolocation = self._get_object(address,name)
            geolocation = GeolocationSerializer(geolocation, many=True).data
            return Response(geolocation)
        except Exception as e:
            return Response({'error': e, 'server_unavailable': True}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request, key=None, format=None):
        
        if request.data.get('id'):
            obj = TblGeolocation.objects.get(id = request.data['id'] )
        
            geolocation = GeolocationSerializer(obj, request.data, partial=True)
        else:
            geolocation = GeolocationSerializer(data=request.data)

        if geolocation.is_valid():
            geolocation.save()
            return Response(status.HTTP_200_OK)
        
        return Response(geolocation.errors, status=status.HTTP_400_BAD_REQUEST)