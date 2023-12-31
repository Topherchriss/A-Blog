from django.urls import path
from . import views
from .views import post_list, post_detail, blog_home
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('home/', blog_home, name='blog_home'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

