from django.urls import path
from .views import user_delete, user_detail_view, user_create, user_index, index, data_create, detail_view, band_list, member_create, jurnal_delete

urlpatterns = [
    path('', index),
    path('create/', data_create),
    path('detail/<int:pk>/', detail_view),
    path('delete/<int:pk>/', jurnal_delete),
    path('bands/', band_list, name='bands'),
    path('member-create/', member_create, name='members'),
    path('users/', user_index),
    path('user_create/', user_create),
    path('user_delete/<int:pk>/', user_delete),
    path('user_detail/<int:pk>/', user_detail_view),
]