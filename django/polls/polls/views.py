from django.http import HttpResponse
from django.shortcuts import render

from . import logic

def render_form(request):
    return render(request, 'polls/poll-submission.html')

def save_vote(request):
    flavor = request.GET["flavor"]
    logic.save_vote(flavor)
    return render(request, 'polls/poll-submission.html')

def render_results(request):
    percent_dict = logic.convert_to_percentages()

    context = {
        "chocolate": percent_dict["chocolate"],
        "vanilla": percent_dict["vanilla"],
        "strawberry": percent_dict["strawberry"],
    }
    
    return render(request, 'polls/summary.html', context)
