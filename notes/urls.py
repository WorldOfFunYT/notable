# ==================================================================================================
# Imports
# ==================================================================================================

from django.urls import path
from . import views

# ==================================================================================================
# Variables
# ==================================================================================================

app_name = 'notes'

# ==================================================================================================
# Code
# ==================================================================================================

# Urls =============================================================================================
# path('url', views.function, name='name')
urlpatterns = [
    path('', views.index, name='index'),
    path('create_note', views.create_note, name='create_note'),
    path('<int:note_id>/delete', views.delete_note, name='delete_note'),
    path('<int:note_id>/', views.edit_note, name='edit_note'),
]
