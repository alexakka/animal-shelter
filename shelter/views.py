from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ShelterCreationForm, LeaveAnApplicationForm
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


@login_required
def shelter_dashboard(request, user_id):
    shelter = get_object_or_404(Shelter, owner=user_id)
    animals = Animal.objects.filter(shelter=shelter.id)

    return render(request, 'adminindex.html', {'animals': animals})


# def leave_application(request, animal_id):
#     if request.method != 'POST':
#         form = LeaveAnApplicationForm()
#     else:
#         form = LeaveAnApplicationForm(data=request.POST)
#         if form.is_valid():
#             new_application = form.save(commit=False)
#             new_application.animal = animal_id
#             new_application.save()

#             return redirect('index')

#     context = {'form': form}
#     return render(request, 'application.html', context)


def leave_application(request, animal_id):
    animal = Animal.objects.get(id=animal_id)

    if request.method == 'POST':
        form = LeaveAnApplicationForm(data=request.POST)
        if form.is_valid():
            new_application = form.save(commit=False)
            new_application.animal = animal
            new_application.save()

            return redirect('index')
    else:
        form = LeaveAnApplicationForm()

    context = {'form': form, 'animal': animal}
    return render(request, 'application.html', context)
