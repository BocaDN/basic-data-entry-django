from django.shortcuts import render, redirect, get_object_or_404
from .models import Actor
from .forms import ActorForm

def actor_list(request):
    actors = Actor.objects.all()
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actor-list')
    else:
        form = ActorForm()

    return render(request, 'actors/actor_list.html', {'form': form, 'actors': actors})

def actor_detail(request, actor_id):
    actor = get_object_or_404(Actor, id=actor_id)
    return render(request, 'actors/actor_detail.html', {'actor': actor})

def toggle_criminal_status(request, actor_id):
    actor = get_object_or_404(Actor, id=actor_id)

    if actor.role != 'suspect':
        return redirect('actor-list')  # Prevent non-suspects from being marked

    if actor.is_criminal:
        actor.is_criminal = False
    else:
        # Ensure no other suspect is marked
        Actor.objects.filter(is_criminal=True).update(is_criminal=False)
        actor.is_criminal = True

    actor.save()
    return redirect('actor-list')

