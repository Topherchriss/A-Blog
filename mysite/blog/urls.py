from django.urls import path
from . import views
from .views import post_list, post_detail
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
