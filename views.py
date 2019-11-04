from django.shortcuts import render, get_object_or_404
from .models import Position, Choice,President
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, 'votingSystem/landingPage.html')


def home(request):
    position = Position.objects.all()
    context = {
        'position': position
    }
    return render(request, 'votingSystem/homepage.html', context)


def candidates(request):
    return render(request, 'candidates/president.html')


class VotesListView(ListView):
    model = President
    template_name = 'votingSystem/homepage.html'
    context_object_name = 'president'


class VotesDetailView(DetailView):
    model = President
    template_name = 'votingSystem/profile.html'
    context_object_name = 'president'


def about(request, president_id):
    president = get_object_or_404(President, pk=president_id)
    return render(request, 'votingSystem/profile.html', {'president': president})


def detail(request, position_id):
    try:
        position = Position.objects.get(pk=position_id)
    except Position.DoesNotExist:
        raise HttpResponse("Position does not exist!")
    return render(request, 'votingSystem/details.html', {'position': position})


def results(request, position_id):
    position = get_object_or_404(Position, pk=position_id)
    return render(request, 'votingSystem/results.html', {'position':position})


def vote(request, position_id):
    position = get_object_or_404(Position, pk=position_id)
    try:
        selected_choice = position.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'votingSystem/details.html', {
            'position': position,
            'error_message':"You didn't select a candidate",
        })
    else:
        selected_choice += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(position.id,)))
