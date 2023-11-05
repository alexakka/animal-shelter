from django.shortcuts import render, get_object_or_404
from .models import Animal


def index(request):
    context = Animal.objects.all().order_by('-id')[:5]

    return render(request, template_name="index.html", context={"context": context})


def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, 'animal_detail.html', {'animal': animal})

