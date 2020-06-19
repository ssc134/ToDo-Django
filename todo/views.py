from django.shortcuts import render
from todo.models import Note
from datetime import datetime
from todo.forms import NewNoteForm
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView


# Create your views here.
def manage(request):
    notesList = Note.objects.all()
    contextDict = {'notes': notesList}
    return render(request, 'todo/manage.html', contextDict)


def new(request):
    form = NewNoteForm()

    if request.method == 'POST':
        form = NewNoteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/todo/manage')
        else:
            print(form.errors)
    return render(request, 'todo/new.html', {'form': form})


def delete(request, id):
    record = Note.objects.get(pk=id)
    record.delete()
    return HttpResponseRedirect("/todo/manage")

'''
def edit(request, id):
    contextDict = {}
    record = Note.objects.get(pk=id)
    contextDict['note'] = record
    form = Ed
    return render(request, 'todo/edit.html', contextDict)
'''
'''
class Edit(UpdateView):
    model = Note
    fields = '__all__'
'''