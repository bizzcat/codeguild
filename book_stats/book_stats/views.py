from . import logic
from django.http import HttpResponse
from django.shortcuts import render

# def render_page(request):
#     """Renders the HTML for some random page."""
#     return HttpResponse('This will be HTML.')


def render_word(request):
    word = request.GET['w']
    if word in logic.word_dict_with_count:
        string = word + ": " + str(logic.word_dict_with_count[word])
    else:
        string =  word + ": 0"
    body = '<html><body>' + string + '</body></html>'

    context = {
        'word': word,
        'count': count,
    }


    return render(request, 'comments/get_word.html', context)




def find_count_for_word(request):
    word = request.GET['w']
    if word in logic.word_dict_with_count:
        string = word + ": " + str(logic.word_dict_with_count[word])
    else:
        string =  word + ": 0"
    body = '<html><body>' + string + '</body></html>'
    return HttpResponse(body)
