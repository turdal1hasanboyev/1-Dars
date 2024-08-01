from django.urls import path

from article.views import user_delete, user_detail_view, user_create, user_index, index, data_create, detail_view, band_list, member_create, jurnal_delete


urlpatterns = [
    path('', index, name="index"),
    path('create/', data_create, name="create"),
    path('detail/<int:pk>/', detail_view, name="detail"),
    path('delete/<int:pk>/', jurnal_delete, name="jurnal_delete"),
    path('bands/', band_list, name='bands'),
    path('member-create/', member_create, name='members'),
    path('users/', user_index, name="users_index"),
    path('user_create/', user_create, name="user_create"),
    path('user_delete/<int:pk>/', user_delete, name="user_delete"),
    path('user_detail/<int:pk>/', user_detail_view, name="user_detail"),
]
