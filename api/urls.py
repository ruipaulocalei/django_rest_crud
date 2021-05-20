from django.contrib import admin
from django.urls import path, include
from .viewsets import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = router.urls
