
from django.urls import path
from . import views
app_name = 'taskapp'

urlpatterns = [

    path('school/',views.school,name='school'),
    path('login/',views.login,name='login'),
    path('newpage/',views.newpage,name='newpage'),
    path('Form',views.Form,name='Form'),
    path('register',views.register,name='register'),



]