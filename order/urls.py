from django.urls import path

from order.views import order_create_view, order_delete_view, order_list_view, order_update_view



urlpatterns = [
    path('order_list/', order_list_view, name='orderlist'),
    path('order_update/<int:pk>/', order_update_view, name='orderupdate'),
    path('order_delete/<int:pk>/', order_delete_view, name='orderdelete'),
    path('order_create/', order_create_view, name='ordercreate'),
]
