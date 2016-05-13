from django.http import HttpResponse
from django.shortcuts import render

from . import logic

def render_submit_page(request):
    return render(request, 'jokes/ajax-submit-page.html')
