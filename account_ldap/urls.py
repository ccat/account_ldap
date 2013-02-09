#from django.conf.urls import patterns, url
from django.conf.urls import patterns, include, url

import account

import conf
from views import *
#from account.views import SignupView, LoginView, LogoutView, DeleteView
#from account.views import ConfirmEmailView
#from account.views import ChangePasswordView, PasswordResetView, PasswordResetTokenView
#from account.views import SettingsView


urlpatterns = patterns("",
    url(r"^signup/$", SignupView.as_view(), name="account_signup"),
    url(r"^password/$", ChangePasswordView.as_view(), name="account_password"),
    url(r"^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$", PasswordResetTokenView.as_view(), name="account_password_reset_token"),
    url(r"^settings/$", SettingsView.as_view(), name="account_settings"),

    url(r"^", include("account.urls")),
)
