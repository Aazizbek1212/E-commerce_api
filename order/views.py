from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from order.models import Order
from order.serializers import OrderSerializer




@api_view(['GET'])
def order_list_view(request):
    item = Order.objects.all()
    serializer = OrderSerializer(item, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def order_create_view(request):
    item = OrderSerializer(data=request.data)
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(item.errors)
    

@api_view(['GET'])
def order_delete_view(request, pk):
    item = Order.objects.get(pk=pk)
    item.delete()
    return Response('')


@api_view(['POST'])   
def order_update_view(request, pk=None):
    item = Order.objects.get(pk=pk)
    item = OrderSerializer(instance=item , data=request.data)
    if item.is_valid():
        item.save()
    else:
        return Response(400)
    return Response(item.data, 200)   