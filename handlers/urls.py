from django.urls import path
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coupons/', views.coupons, name='coupons'),
    path('addcoupons/', views.addcoupon, name='addcoupon'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)