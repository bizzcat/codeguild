from django.shortcuts import render
from . import logic


def render_index(request):
    flut_list_ten = logic.get_ten_recent_fluts()

    template_args = {
        'flut_list': flut_list_ten,
    }
    return render(request, 'flutter/index.html', template_args)

def save_flut_and_render_ack(request):
    user_name = request.POST['user_name']
    flut_text = request.POST['flut_text']
    logic.save_new_flut(user_name, flut_text)

    template_args = {
        'user_name': user_name,
        'flut_text': flut_text,
    }
    return render(request, 'flutter/ack.html', template_args)


def render_user_page(request, user_name):
    fluts_to_user = logic.get_all_fluts_for_user(user_name)

    template_args = {
        'user_name': user_name,
        'fluts_to_user': fluts_to_user,
    }
    return render(request, 'flutter/user_page.html', template_args)



def render_search_results(request):
    search_text = request.GET['search_text']
    fluts_to_search = logic.find_fluts_for_search(search_text)

    template_args = {
        'search_text': search_text,
        'fluts_to_search': fluts_to_search,
    }
    return render(request, 'flutter/search_page.html', template_args)
