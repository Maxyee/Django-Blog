from django.urls import path
# from contacts import views as contact_view
from posts import views as post_view

urlpatterns = [
    path('', post_view.post_list),
    path('create/', post_view.post_create),
    path('detail/<int:id>/', post_view.post_detail, name='detail'),
    path('update/', post_view.post_update),
    path('delete/', post_view.post_delete),
]