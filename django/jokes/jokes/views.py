
from django.http import HttpResponse
from django.shortcuts import render

from . import logic

def render_submit_page(request):
    return render(request, 'jokes/submit-page.html')

def cycle_submit_page(request):
    logic.save_joke(request.POST['joke-setup'], request.POST['joke-punchline'])
    return render(request, 'jokes/submit-page.html')

def render_listing_page(request):
    jokes = logic.get_all_jokes()
    context = {
        'jokes': jokes,
    }
    return render(request, 'jokes/listing-page.html', context)
