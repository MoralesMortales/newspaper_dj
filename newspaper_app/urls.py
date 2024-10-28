
from django.urls import path
from .views import chooseToEdit, mainView, createNew, chooseToDelete, deleteOne, editing

urlpatterns = [
    path('', mainView, name="main"),
    path('create', createNew, name="create"),
    path('edit', createNew, name="create"),
    path('delete', chooseToDelete, name="choose_delete"),
    path('edit_choose', chooseToEdit, name="choose_edit"),
    path('editing/<int:id>', editing, name='editing'),
    path('delete/<int:id>', deleteOne, name="delete")
]
