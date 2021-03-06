from django.db.models.fields import CommaSeparatedIntegerField
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Superhero


#* Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def details(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/details.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary')
        secondary_ability = request.POST.get('secondary')
        catch_phrase = request.POST.get('catch_phrase')

        #?Instantiate Superhero Objects
        new_hero = Superhero(
            name = name, 
            alter_ego = alter_ego,
            primary_ability = primary_ability, 
            secondary_ability = secondary_ability, 
            catch_phrase = catch_phrase,
        )

        #?save to Superhero DB
        new_hero.save()
        #?return user to superheroes/index.html
        return HttpResponseRedirect(reverse('superheroes:index'))

    else:
        return render(request, 'superheroes/create.html')

def edit(request, hero_id):
    edit_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'edit_hero': edit_hero
    }

    if request.method == "POST":
        edit_hero.name = request.POST.get('name')
        edit_hero.alter_ego = request.POST.get('alter_ego')
        edit_hero.primary_ability = request.POST.get('primary')
        edit_hero.secondary_ability = request.POST.get('secondary')
        edit_hero.catch_phrase = request.POST.get('catch_phrase')
        
        #?save to Superhero DB
        edit_hero.save()
        #?return user to superheroes/index.html
        return HttpResponseRedirect(reverse('superheroes:index'))
        
    else:
        return render(request, 'superheroes/edit.html', context)

def delete(request, hero_id):
    del_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'del_hero': del_hero
    }

    if request.method == "POST":
        del_hero.delete()
        #?return user to superheroes/index.html
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/delete.html', context)