from django.urls import path
from login.views import *

urlpatterns = [
    path('', User_Login.as_view(),name='user_login'),
    path('user_registration/', User_Registraion.as_view(),name='user_registration'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(),name='activate'),
    path('forgot_password',forgot_password,name='forgot_password'),


    path('send_otp',send_otp,name='send_otp'),
    path('enter_otp',enter_otp,name='enter_otp'),
    path('password_reset',password_reset,name='password_reset')
]