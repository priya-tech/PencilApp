from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AddNotesForm
from .models import AddNotesModel
from django.urls import reverse
# Create your views here.

def add_note(request):
    if request.method=='POST':
        form=AddNotesForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('view_notes'))

    else:
        form=AddNotesForm()
        return render(request, 'notes/add.html', {'form':form})


def view_note(request):
    notes=AddNotesModel.objects.all()
    return render(request, 'notes/view.html', {'all_notes':notes})

def delete_note(request,id):
    AddNotesModel.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('view_notes'))

def edit_note(request,**kwargs):
    if kwargs['action']=='edit':
        data={}
        notes=AddNotesModel.objects.all()
        data['notes']=notes
        data['id']=kwargs['id']
        return render(request, 'notes/edit.html', {'data':data})
    if kwargs['action']=='submit':
        note=AddNotesModel.objects.get(id=kwargs['id'])
        note.text=request.GET.get('note')
        note.save()
        return HttpResponseRedirect(reverse('view_notes'))
