from . import logic
from django.http import HttpResponse


def find_count_for_word(request):
    word = request.GET['w']
    if word in logic.word_dict_with_count:
        string = word + ": " + str(logic.word_dict_with_count[word])
    else:
        string =  word + ": 0"
    body = '<html><body>' + string + '</body></html>'
    return HttpResponse(body)
