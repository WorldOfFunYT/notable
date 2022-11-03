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
    path('logout/', views.logout_user, name='logout_user'),
    path('login/', views.login_view, name='login_view'),
    path('login_user/', views.login_user, name='login_user'),
    path('signup/', views.signup_view, name='signup_view'),
    path('signup_user/', views.create_user, name='signup_user'),
]
