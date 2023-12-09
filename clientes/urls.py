from django.urls import path
from . import views
from django.urls import re_path


urlpatterns = [
    re_path('login/cliente/', views.cliente_login, name='cliente_login'),
    re_path('v2admin/registrar/cliente', views.create_client, name='create_client'),
    re_path('v2admin/login/', views.admin_login, name='admin_login'),
    re_path('v2/cliente_dashboard/', views.cliente_dashboard, name='cliente_dashboard'),
    re_path('upload', views.upload_file, name='upload_file'),
    re_path('v2/cliente_citas/', views.cliente_citas, name='cliente_citas'),
    re_path('logout/', views.logout_view, name='logout'),
    re_path('crear-admin/', views.create_admin, name='create_admin'),
    re_path('settings/notifications', views.notification_settings, name='notification_settings'),
    re_path('eliminar-notificacion/<int:id_notificacion>', views.eliminar_notificacion, name='eliminar_notificacion'),
]
