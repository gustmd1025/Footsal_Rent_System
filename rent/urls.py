from django.urls import path
from . import views

app_name = 'rent'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:place_id>/', views.detail, name='detail'),
    path('place/create/', views.place_create, name='place_create'),
    path('place/modify/<int:place_id>/', views.place_modify, name='place_modify'),
    path('place/delete/<int:place_id>/', views.place_delete, name='place_delete'),
    path('rentinfo/', views.info_index, name='rentinfo_index'),
]