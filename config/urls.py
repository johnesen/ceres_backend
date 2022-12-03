from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/docs/', include_docs_urls(title='CeresAPI')),
    path('api/', include('users.urls'), name='auth'),
    path('api/', include('news.urls'), name='articles'),
    path('api/', include('products.urls'), name='products'),
    path('api/', include('catalogs.urls'), name='catalogs'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

