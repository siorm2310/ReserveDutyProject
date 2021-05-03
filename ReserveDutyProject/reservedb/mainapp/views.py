from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Person
from .forms import PersonForm
import csv

def home(request):
    person_list = Person.objects.all().order_by('name', 'rank')
    return render(request, 'mainapp/home.html', {"person_list":person_list})

def search(request, search_name):
    person_list = Person.objects.filter(name__icontains=search_name).order_by('name', 'rank')
    return render(request, 'mainapp/home.html', {"person_list":person_list})

def add(request):
    person_list = Person.objects.all().order_by('name', 'rank')

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PersonForm()
    
    if 'submit' in request.POST:
        return HttpResponseRedirect('/')
    elif 'add_more' in request.POST:
        return HttpResponseRedirect('/add/')

    return render(request, 'mainapp/add.html', {"person_list":person_list, "form":form})

def update(request, wanted_id):
    person_list = Person.objects.all().order_by('name', 'rank')
    wanted_person = Person.objects.get(id=wanted_id)
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            updatedPerson = form.cleaned_data
            wanted_person.name = updatedPerson['name']
            wanted_person.rank = updatedPerson['rank']
            wanted_person.group = updatedPerson['group']
            wanted_person.last_here = updatedPerson['last_here']
            wanted_person.save()
            return HttpResponseRedirect('/')
    else:
        form = PersonForm(instance=wanted_person) 

    return render(request, 'mainapp/update.html', {'person_list':person_list, 'form':form})

def delete(request, wanted_id):
    person_list = Person.objects.all().order_by('name', 'rank')
    wanted_person = Person.objects.get(id=wanted_id)
    if request.method == 'POST':
        wanted_person.delete()
        return HttpResponseRedirect('/')
    return render(request, 'mainapp/delete.html', {'person_list':person_list})

def export_users_csv(request, search_name=''):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="personnel.csv"'
    response.write(u'\ufeff'.encode('utf8'))

    writer = csv.writer(response)
    writer.writerow(['שם', 'דרגה', 'מדור', 'תאריך אחרון'])

    personnel = Person.objects.filter(name__icontains=search_name)
    for person in personnel:
        writer.writerow([person.name, person.get_group_display(), person.get_rank_display(), person.last_here])

    return response