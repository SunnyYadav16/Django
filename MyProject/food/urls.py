from django.urls import path
from . import views
 
app_name = "food"
urlpatterns = [
    # path("", views.index, name='index'),
    path("", views.IndexClassView.as_view(), name='index'),
    # path("detail-view/<int:item_id>/", views.detail_view, name='detail'),
    path("detail-view/<int:pk>/", views.DetailClassView.as_view(), name='detail'),
    path("add-item/", views.CreateItemView.as_view(), name='create_item'),
    path("update-item/<int:item_id>/", views.update_item, name='update_item'),
    path("delete-item/<int:item_id>/", views.delete_item, name='delete_item'),
]
