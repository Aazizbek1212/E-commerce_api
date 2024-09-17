from django.urls import path

from main.views import category_create_view, category_destroy_view, category_list_view, category_update_view, create_view, destroy_view, list_view, update_view



urlpatterns = [
    path('list/', list_view, name='list'),
    path('update/<int:pk>/', update_view, name='update'),
    path('delete/<int:pk>/', destroy_view, name='destroy'),
    path('create/', create_view, name='create'),
    path('category_lit/', category_list_view, name='categorylist'),
    path('category_update/<int:pk>/', category_update_view, name='categoryupdate'),
    path('category_delete/', category_destroy_view, name='categorydelete'),
    path('category_create', category_create_view, name='categorycreate'),
]
