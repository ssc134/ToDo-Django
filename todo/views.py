from django.shortcuts import render
from todo.models import Note

# Create your views here.
def manage(request):
    notesList = Note.objects.all()
    contextDict = {'notes':notesList}
    return render(request, 'todo/manage.html', contextDict)