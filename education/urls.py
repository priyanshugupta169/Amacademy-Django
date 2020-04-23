from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('index.html', views.index , name ='index'),
    path('', views.index , name ='index'),
    # path('login.html', views.login , name ='login'),
    path('contact.html', views.contact , name ='contact'),
    path('about.html', views.about , name ='about'),
    # path('AdminLogin.html', views.adminlogin , name ='AdminLogin'),
    path('doubts.html', views.doubts , name ='doubts'),
    # path('ChangePassword.html', views.changepass , name ='ChangePassword'),
    # path('forgetpass.html', views.forgetpass , name ='forgetpass'),
    # path('register.html', views.register , name ='register'),
    # path('ForgotAdminPass.html', views.forgotadminpass , name ='forgotadminpass'),
    # path('registeradmin.html', views.registeradmin , name ='registeradmin'),
    path('specificfile.html/<str:course_name>', views.specificfile , name ='specificfile'),
    path('readfile.html/file=<str:filename>', views.pdf_view , name ='pdf_view'),
    path('download.html/file=<str:filename>', views.download , name ='download'),
    path('delete.html/file=<str:filename>', views.delete , name ='delete'),
    # url(r'^pdf',views.pdf_view,name='pdf_view'),
    # path('pdf_view.html/uploads/<str:filename>', views.pdf_view , name ='pdf_view'),
]