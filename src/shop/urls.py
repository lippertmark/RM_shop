from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('products/', views.all_products, name='all_products'),
    path('products/<str:category>/', views.all_products_by_category, name='all_products_category'),
    path('main_page/', views.main_page, name='main_page'),
    path('menu/', views.menu, name='menu'),
    path('sale/', views.sale_products, name='sale'),
    path('delivery/', views.delivery, name='delivery')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)