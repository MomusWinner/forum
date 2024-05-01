from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'section', views.SectionViewSet)
router.register(r'thread', views.ThreadViewSet)
router.register(r'message', views.MessageViewSet)

urlpatterns = [
    path('api/', include(router.urls), name='api'),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path('register/', views.register, name='register'),
]