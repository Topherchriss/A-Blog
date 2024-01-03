from django.urls import path
from . import views
from .views import post_list, post_detail, blog_home, add_comment, user_logout, user_login, user_signup

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('home/', blog_home, name='blog_home'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', login_required(views.post_edit), name='post_edit'),
    path('add_comment/<int:post_pk>/', views.add_comment, name='add_comment'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),

]

if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

