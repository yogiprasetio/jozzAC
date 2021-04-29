from django.urls import path
from .views import pesananKhusus, Tracking

app_name = 'pesanan'

urlpatterns = [
	path('admin/add-khusus/', pesananKhusus.as_view(), name='add_khusus'),
	path('admin/tracking/', Tracking.as_view(), name='tracking'),
]