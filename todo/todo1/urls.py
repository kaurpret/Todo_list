from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.todo , name='todo'),
    path('submit', views.submit , name='todo1'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('edit/<int:id>', views.edit,name='edit'),
    path('update/<int:id>', views.update,name='update'),
    path('list_item', views.list_item,name='list_item'),
    path('sort', views.sort,name='sort'),
    path('search', views.search,name='search'),
]