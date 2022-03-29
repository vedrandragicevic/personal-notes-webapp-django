from asyncio import selector_events
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
from django.http import HttpResponseRedirect
from django.contrib import messages


@login_required(login_url='login')
def notes(request):
    # all_notes = Note.objects.all()
    profile = request.user.profile
    all_notes = profile.note_set.all()

    context = {
        'all_notes': all_notes
    }

    return render(request, 'notes/notes.html', context)


@login_required(login_url='login')
def completed_notes(request):
    # all_notes = Note.objects.all()
    profile = request.user.profile
    all_notes = profile.note_set.all()
    completed_notes = all_notes.filter(completed_flag=True)

    context = {
        'completed_notes': completed_notes
    }

    return render(request, 'notes/completed_notes.html', context)


@login_required(login_url='login')
def update_completed_flag(request, pk):
    selected_note = Note.objects.get(id=pk)
    selected_note.completed_flag = True
    selected_note.save()

    return redirect('mynotes')


@login_required(login_url='login')
def track_note(request, pk):
    selected_note = Note.objects.get(id=pk)
    selected_note.completed_flag = False
    selected_note.save()

    return redirect('completed-notes')


@login_required(login_url='login')
def delete_note(request, pk):
    profile = request.user.profile
    note = profile.note_set.get(id=pk)
    if request.method == 'POST':
        note.delete()
        # messages.success(request, 'Note was deleted!')
        return redirect('mynotes')

    context = {'object': note}

    return render(request, 'delete_template.html', context)


@login_required(login_url='login')
def create_note(request):
    profile = request.user.profile
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = profile
            note.save()
            # messages.success(request, 'Note was created!')
            return redirect('mynotes')

    context = {'form': form}
    return render(request, 'notes/note_form.html', context)
