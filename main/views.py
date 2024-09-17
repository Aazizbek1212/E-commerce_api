from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Category, Product
from main.serializers import CategorySerializer, ProductSerializer





@api_view(['GET'])
def list_view(request):
    item = Product.objects.all()
    serializer = ProductSerializer(item, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def destroy_view(request, pk=None):
    item = Product.objects.get(pk=pk)
    item.delete()
    return Response("item o'chirildi")


@api_view(['POST'])
def create_view(request):
    item = ProductSerializer(data=request.data)
    if item.is_valid():
        item.save()
        return Response("item qo'shildi", 201)
    else:
        return Response(item.errors)


@api_view(['POST'])   
def update_view(request, pk=None):
    item = Product.objects.get(pk=pk)
    item = ProductSerializer(instance=item , data=request.data)
    if item.is_valid():
        item.save()
    else:
        return Response(400)
    return Response(item.data, 200)



@api_view(['GET'])
def category_list_view(request):
    item = Category.objects.all()
    serializer = CategorySerializer(item, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def category_create_view(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response('Category yaratildi' , serializer.data)
    else:
        return Response(serializer.errors)
    

@api_view(['GET'])
def category_destroy_view(request, pk=None):
    category = Category.objects.get(pk=pk)
    category.delete()
    return Response("category o'chirildi")


@api_view(['POST'])   
def category_update_view(request, pk=None):
    category = Category.objects.get(pk=pk)
    category = CategorySerializer(instance=category , data=request.data)
    if category.is_valid():
        category.save()
    else:
        return Response(400)
    return Response(category.data, 200)