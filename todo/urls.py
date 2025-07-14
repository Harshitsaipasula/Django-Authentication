from django.urls import path
from .views import TodoCreateView, TodoListView, TodoDeleteView, TodoUpdateView

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("create/", TodoCreateView.as_view(), name="todo_create"),
    path("update/", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/", TodoDeleteView.as_view(), name="todo_delete"),
]
