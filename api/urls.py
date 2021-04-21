from django.urls import include, path
from rest_framework import routers
from . import views
urlpatterns = [
    path('',views.api_overview,name='api-overview'),
    path('mark-digitized',views.update_status,name='mark-digitized'),
    path('update-invoice',views.add_invoice,name='update-invoice'),
    path('upload-invoice',views.upload_invoice,name='upload-invoice'),
    path('status/<int:invoiceNum>',views.get_status,name='get-status'),
    path('get-invoice/<int:invoiceNum>',views.get_invoice,name='get-invoice'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]