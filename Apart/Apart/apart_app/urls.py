from django.urls import path

from Apart.apart_app.views import create_apart, edit_apart, apart_details, home_page, delete_apart, all_aparts

urlpatterns = [
    path('', home_page, name='home page'),
    path('create/',create_apart, name='create'),
    path('all/', all_aparts, name='all aparts'),
    path('details/<int:pk>', apart_details, name='apart details'),
    path('edit/<int:pk>', edit_apart, name='edit'),
    path('delete/<int:pk>', delete_apart, name='delete'),
]