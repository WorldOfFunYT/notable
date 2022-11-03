from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *
from .forms import *

# Create your views here.
@login_required(login_url='/notes/login')
def index(request):
    noteList = request.user.note_set.all()
    context = {
        'notes': noteList,
    }
    return render(request, 'notes/index.html', context)

@login_required(login_url='/notes/login')
def create_note(request):
    if request.method == 'POST':
        form_data = request.POST
        note = Note(title=form_data['title'], text=form_data['note-content'], user=request.user)
        note.save()
        return HttpResponseRedirect('/notes')
    else:
        form = NoteForm()
    context = {'form': form}
    return render(request, 'notes/create_note.html', context)

@login_required(login_url='/notes/login')
def delete_note(request, note_id):
    print(f'Note_id: {note_id}')
    note = Note.objects.get(id=note_id)
    note.delete()
    return HttpResponseRedirect('/notes')

@login_required(login_url='/notes/login')
def edit_note(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == 'POST':
        form_data = request.POST
        note.title = form_data['title']
        note.text = form_data['note-content']
        note.save()
        return HttpResponseRedirect('/notes')
    context = {'note': note}
    return render(request, 'notes/edit_note.html', context)

@login_required(login_url='/notes/login')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/notes/login')

def login_view(request):
    context = {}
    return render(request, 'notes/login.html', context)

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/notes')
    else:
        messages.add_message(request, messages.ERROR, 'Account doesn\'t exist. Maybe sign up?')
        return HttpResponseRedirect('/notes/login') 

def signup_view(request):
    context = {}
    return render(request, 'notes/signup.html', context)

def create_user(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        check_for_user = User.objects.get(username=username)
    except:
        user = User.objects.create_user(username=username, password=password)
        user.save()
        login(request, user)
        return HttpResponseRedirect('/notes')


    messages.add_message(request, messages.ERROR, 'Account with that username already exists, choose another username.')
    return HttpResponseRedirect('/notes/signup')
