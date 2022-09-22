# ==================================================================================================
# Imports
# ==================================================================================================

from django.db import models
from django.contrib.auth.models import User

# ==================================================================================================
# Note
# ==================================================================================================

class Note(models.Model):
    title = models.CharField('Note Title', max_length=100)
    text = models.CharField('Note Text', max_length=500)
    dateWritten = models.DateField('Date Written')
    user = models.ForeignKey("User", verbose_name=("Note Author"), on_delete=models.CASCADE)