from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-donor',views.AddDonorView.as_view(),name='add-donor'),
    path('list-donor',views.ListDonorView.as_view(),name='list-donor'),
    path('delete-donor/<int:pk>',views.DeleteDonorView.as_view(),name='delete-donor'),
    path('update-donor/<int:pk>',views.UpdateDonorView.as_view(),name='update-donor'),

]
