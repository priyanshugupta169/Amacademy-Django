from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
     path('register.html', views.register , name ='register'),
     path('login.html', views.login , name ='login'),
     path('registeradmin.html', views.registeradmin , name ='registeradmin'),
     path('forgetpass.html', views.forgetpass , name ='forgetpass'),
     path('OTPverification.html', views.otpverify , name ='OTP_Verify'),
     path('AdminLogin.html', views.adminlogin , name ='AdminLogin'),
    #  path('ForgotAdminPass.html', views.forgotadminpass , name ='forgotadminpass'),
    path('ChangePassword.html', views.changepass , name ='ChangePassword'),
    path('logout', views.logout , name ='logout'),
    
]