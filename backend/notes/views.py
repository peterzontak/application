import os
from django.shortcuts import render, HttpResponse
from notes.controller.poznamky import get_notes_categories, get_note


def notes_show_view(request, note: str):
    dir_path = './poznamky/' + note
    notes = get_notes_categories()
    # dirs = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))]
    # files = [d for d in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, d))]
    data = get_note(note)
    
    # print(data['dirs'])
    # print(note,dirs,files)
    return render(request, 'notes/show.html', {'notes': notes, 'data': data, 'note': note})
