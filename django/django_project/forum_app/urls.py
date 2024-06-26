"""URL configuration for forum project."""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('section', views.SectionViewSet)
router.register('thread', views.ThreadViewSet)
router.register('message', views.MessageViewSet)
router.register('user', views.UserViewSet)

schema_view = get_schema_view(
   openapi.Info(
    title='Snippets API',
    default_version='v1',
    description='Test description',
    terms_of_service='https://www.google.com/policies/terms/',
    contact=openapi.Contact(email='contact@snippets.local'),
    license=openapi.License(name='BSD License'),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),
    path('martor/', include('martor.urls')),
    re_path('^api/v1/', include('djoser.urls')),
    re_path('^api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include(router.urls), name='api'),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
