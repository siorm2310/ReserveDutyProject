from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/<search_name>/', views.search, name='search'),
    path('add/', views.add, name='add'),
    path('update/<int:wanted_id>/', views.update, name='update'),
    path('delete/<int:wanted_id>/', views.delete, name='delete'),
    path('export/csv/', views.export_users_csv, name='export_users_csv'),
    path('export/csv/<search_name>/', views.export_users_csv, name='export_users_csv'),
]