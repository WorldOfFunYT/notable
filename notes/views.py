from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import *
from .forms import *

# Create your views here.

def index(request):
    noteList = request.user.note_set.all()
    context = {
        'notes': noteList,
    }
    return render(request, 'notes/index.html', context)

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

def delete_note(request, note_id):
    print(f'Note_id: {note_id}')
    note = Note.objects.get(id=note_id)
    note.delete()
    return HttpResponseRedirect('/notes')

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