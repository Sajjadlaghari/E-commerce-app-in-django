"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ecommerce import views

urlpatterns = [
    path('admin/', include('admin.urls')),
    path('',include('home.urls')),
    path('product/',include('products.urls')),
    path('accounts/',include('accounts.urls')),
    path('add-to-cart',views.ProductAddToCart),
    path('products-cart',views.ViewCartProducts),
    path('remove-product-cart/<id>',views.DeletProductFromCart),
    path('book-order',views.BookOrdered),
    path('confirm-ordered',views.ConfirmOrdered),
    path('checkout', views.HomePageView.as_view(), name='home'),
    path('success', views.success,name='success'),
    # path('create-checkout-session', views.create_checkout_session, name='checkout'),
    # path('success.html/', views.success,name='success'),
    path('cancel.html/', views.cancel,name='cancel'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
