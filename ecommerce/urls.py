"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path,include  
from django.conf.urls.static import static
from app.forms import LoginForm, MyPasswordResetForm, MySetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')), 

      # login authentication
  path('login/', auth_views.LoginView.as_view( template_name='login.html', authentication_form=LoginForm ), 
    name='login'),

  path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
  

  path('changepassword/', auth_views.PasswordChangeView.as_view(
    template_name='changepassword.html',
    form_class=UserPasswordChangeForm,
    success_url='/passwordchangedone'  # Ensure this is correct
), name='changepassword'),

  path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view
    (template_name='passwordchangedone.html'),
    name='passwordchangedone'),

    #  password reset urls
  path('password_reset/', auth_views.PasswordResetView.as_view
    (template_name='resetpassword.html',form_class=MyPasswordResetForm) ,
    name='password_reset'),

  path('password_reset/done/', auth_views.PasswordResetDoneView.as_view
    (template_name='resetpassworddone.html') ,
    name='password_reset_done'),

  path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view
    (template_name='resetpasswordconfirm.html',form_class=MySetPasswordForm) ,
    name='password_reset_confirm'),

  path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view
    (template_name='password_reset_complete.html'),name='password_reset_complete'),

 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

