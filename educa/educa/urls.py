"""educa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from courses.views import CourseListView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from courses import views
from courses.views import dashboard
from agora.views import Agora
from courses.views import register
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(),
         name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),
         name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls')),
    path('', CourseListView.as_view(), name='course_list'),
# reset password urls
    #path('', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('students/', include('students.urls')),
    path('api/', include('courses.api.urls', namespace='api')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('agora/',Agora.as_view(app_id='03a5634c4c0540d5b77d1cd1ceac74a9', channel='elearning_chnl1')),
    path('news/', include('newsapp.urls')),
    path('chat/', include('chat.urls', namespace='chat')),
    #path('about/', include('courses.urls')),
    #path('contact/', include('courses.urls')),
    #path('news/', include('courses.urls')),
    #path('account/', include('account.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
