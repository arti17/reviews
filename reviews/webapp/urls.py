from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('product/create/', views.ProductCreateView.as_view(), name='create_product'),
    path('product/<int:pk>/', views.ProjectDetailView.as_view(), name='detail_product'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='update_product'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete_product'),
]
