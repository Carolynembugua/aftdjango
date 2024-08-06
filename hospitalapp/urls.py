from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('index/', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctor, name='doctors'),
    path('appointment/', views.appointment, name='appointment'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('direct/',views.direct,name='direct'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('', views.register, name='register'),
    path('login/',views.login,name='login'),


]
