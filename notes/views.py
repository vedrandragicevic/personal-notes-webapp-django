from asyncio import selector_events
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


@login_required(login_url='login')
def notes(request):
    # all_notes = Note.objects.all()
    profile = request.user.profile
    notes = profile.note_set.all()
    all_notes = notes.filter(completed_flag=False)

    # PAGINATION IMPLEMENTATION
    note_paginator = Paginator(all_notes, 10)
    page = request.GET.get('page')

    try:
        notes_paginated = note_paginator.page(page)
    except PageNotAnInteger:
        page = 1
        notes_paginated = note_paginator.page(page)
    except EmptyPage:
        page = note_paginator.num_pages
        notes_paginated = note_paginator.page(page)

    left_index = int(page) - 4
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5
    if right_index > note_paginator.num_pages:
        right_index = note_paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    context = {
        'all_notes': all_notes,
        'notes_paginated': notes_paginated,
        'custom_range': custom_range
    }

    return render(request, 'notes/notes.html', context)


@login_required(login_url='login')
def completed_notes(request):
    # all_notes = Note.objects.all()
    profile = request.user.profile
    all_notes = profile.note_set.all()
    completed_notes = all_notes.filter(completed_flag=True)

    # PAGINATION IMPLEMENTATION
    note_paginator = Paginator(completed_notes, 10)
    page = request.GET.get('page')

    try:
        completed_notes_paginated = note_paginator.page(page)
    except PageNotAnInteger:
        page = 1
        completed_notes_paginated = note_paginator.page(page)
    except EmptyPage:
        page = note_paginator.num_pages
        completed_notes_paginated = note_paginator.page(page)

    left_index = int(page) - 4
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5
    if right_index > note_paginator.num_pages:
        right_index = note_paginator.num_pages + 1

    custom_range = range(left_index, right_index)


    context = {
        'completed_notes': completed_notes,
        'notes_paginated': completed_notes_paginated,
        'custom_range': custom_range
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


def single_note(request, pk):
    profile = request.user.profile
    note = profile.note_set.get(id=pk)

    context = {
        'note': note
    }
    return render(request, 'notes/single_note.html', context)