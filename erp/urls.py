from django.urls import path, include
from rest_framework import routers
from . import views
from .views import *

router = routers.DefaultRouter()
router.register('coa', views.CoaViewSet)
router.register('product', views.ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index),
    path('coa/', views.CoaList.as_view(), name='coa_list'),
    path('coa/<int:pk>/', views.CoaDetail.as_view()),
    path('coa/<int:pk>/delete/', views.delete_coa),
    path('coa/create/', views.create_coa, name='coa_create'),
    path('coa/<int:pk>/update/', views.update_coa, name='coa_update'),
    path('product/', views.ProductList.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('product/<int:pk>/delete/', views.delete_product),
    path('product/create/', views.create_product, name='product_create'),
    path('product/<int:pk>/update/', views.update_product, name='product_update'),

    # path('coa/', CoaList.as_view()),
    # path('coa/<int:id>/', CoaDetail.as_view()),
    # path('product/', ProductList.as_view()),
    # path('product/<int:id>/', ProductList.as_view()),

]