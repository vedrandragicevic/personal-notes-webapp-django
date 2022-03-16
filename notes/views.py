from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Note


# Create your views here.


def notes(request):
    all_notes = Note.objects.all()
   
    context = {
        'all_notes': all_notes
    }
    
    print("Rendering notes template...")
    return render(request, 'notes/notes.html', context)
