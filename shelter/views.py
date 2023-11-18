from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ShelterCreationForm
from .models import Shelter, Animal


def index(request):
    context = Animal.objects.all().order_by('-id')[:10]

    return render(request, template_name="index.html", context={"context": context})


def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, 'animal_detail.html', {'animal': animal})


@login_required
def create_shelter(request):
    if request.method != 'POST':
        form = ShelterCreationForm()
    else:
        form = ShelterCreationForm(data=request.POST)
        if form.is_valid():
            new_shelter = form.save(commit=False)
            new_shelter.owner = request.user
            new_shelter.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'create_shelter.html', context)
