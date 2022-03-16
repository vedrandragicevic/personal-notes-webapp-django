from asyncio import selector_events
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Note
from django.http import HttpResponseRedirect


@login_required
def notes(request):
    all_notes = Note.objects.all()
    current_user = request.user
    print (current_user.id)
    # TODO - IMPLEMENT THIS FILTER
    # all_notes = Note.objects.filter(owner = current_user.id)
   
    context = {
        'all_notes': all_notes
    }

    print("Rendering notes template...")
    return render(request, 'notes/notes.html', context)


@login_required
def updateCompletedFlagNote(request, pk):
    selected_note = Note.objects.get(id=pk)
    selected_note.completed_flag = True
    selected_note.save()
    return redirect('mynotes')