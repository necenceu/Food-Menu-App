from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    # main page of the website
    path('', views.index, name='index'),

    # detail of item
    path('<int:item_id>/', views.detail, name='detail'),

    # some item path to test fucntionality
    path('item/', views.item, name='item'),

    # adding item
    path('add', views.add_item, name='add_item'),

    # editing item
    path('update/<int:id>/', views.update_item, name='update_item'),

    # deleting item
    path('delete/<int:id>/', views.delete_item, name='delete_item'), 
]