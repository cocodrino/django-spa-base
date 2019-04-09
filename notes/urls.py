from django.urls import path
from .views import notes_list, note_add

urlpatterns = [
    path('<int:user>/tasks/', notes_list),
    path('tasks/new', note_add)
]
