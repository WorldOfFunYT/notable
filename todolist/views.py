from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *

# Create your views here.
@login_required(login_url='/notes/login')
def index(request):
    toDoLists = request.user.list_set.all()
    context = {
        'toDoLists': toDoLists,
    }
    
    return render(request, 'todo/index.html', context)

def toggle_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.is_complete = not item.is_complete
    item.save()
    return HttpResponseRedirect('/todo')

def delete_list(request, list_id):
    list_object = List.objects.get(id=list_id)
    list_object.delete()
    return HttpResponseRedirect('/todo')

def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return HttpResponseRedirect('/todo')

def create_item(request, list_id):
    print(list_id)
    toDoLists = request.user.list_set.all()
    if request.method == 'POST':
        form_data = request.POST
        item = Item(title=form_data['title'], user=request.user, parent_list=list_id)
        item.save()
        return HttpResponseRedirect('/todo')
    else:
        context = {'toDoLists': toDoLists, 'chosen_list_id':list_id+1}

    return render(request, 'todo/create_item.html', context)