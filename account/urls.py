from django.conf.urls import url
from django.urls import path,include,re_path
from . import views
from django.contrib.auth import  views as auth_views
from django.urls import reverse_lazy
app_name='account'
#2.0开始namespace设置app_name
urlpatterns=[
  # path(r'login/', views.user_login,name='user_login'),
    path(r'login/',  auth_views.LoginView.as_view(template_name="registration/login.html"), name='user_login'),
    path(r'new_login/', auth_views.LoginView.as_view(template_name="account/login.html"), name='user_login'),
    path(r'logout/',  auth_views.LoginView.as_view(template_name="account/logout.html"), name='user_logout'),
    path(r'register/', views.register, name='user_register'),
    path('password-change/',auth_views.PasswordChangeView.as_view(template_name='account/password_change_form.html',
        success_url=reverse_lazy('account:password_change_done')),name='password_change'),
    path('password-change-done/',auth_views.PasswordChangeDoneView.as_view(
        template_name='account/password_change_done.html'),name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='account/password_reset_form.html',email_template_name='account/password_reset_email.html',subject_template_name='account/password_reset_subject.txt',success_url='/account/password_reset_done/',from_email='linqiang@eastcom.com'),name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),name='password_reset_done'),
    re_path('password_reset_confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html',success_url='/account/password_reset_complete/'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),name='password_reset_complete'),
]