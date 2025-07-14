from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Todo

class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = "todo/list.html"
    context_object_name = "todos"
    
    def get_queryset(self):
        # Only show todos for the current user
        return Todo.objects.filter(user=self.request.user)

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = "todo/create.html"
    fields = ['title', 'description']
    success_url = reverse_lazy("todo_list")
    
    def form_valid(self, form):
        # Automatically set the user to the current logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = "todo/update.html"
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy("todo_list")
    
    def get_queryset(self):
        # Only allow users to update their own todos
        return Todo.objects.filter(user=self.request.user)

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = "todo/delete.html"
    success_url = reverse_lazy("todo_list")
    
    def get_queryset(self):
        # Only allow users to delete their own todos
        return Todo.objects.filter(user=self.request.user)