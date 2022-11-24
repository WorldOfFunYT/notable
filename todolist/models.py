# ==================================================================================================
# Imports
# ==================================================================================================

from django.db import models
from django.contrib.auth.models import User

# ==================================================================================================
# Models
# ==================================================================================================



class List(models.Model):
    title = models.CharField('List Title', max_length=100)
    description = models.CharField('List Description', max_length=500)
    dateWritten = models.DateTimeField('Date Written', auto_now_add=True)
    user = models.ForeignKey(User, verbose_name=("List Creator"), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Item(models.Model):
    title = models.CharField('Item Title', max_length=100)
    list_group = models.ForeignKey(List, verbose_name=("parent_list"), on_delete=models.CASCADE)
    is_complete = models.BooleanField()
    user = models.ForeignKey(User, verbose_name=("Item Creator"), on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.title}" from "{self.list_group.title}"'