from . import models


def save_new_flut(user_name, flut_text):
    new_flut = models.Flut(
        user_name=user_name,
        flut_text=flut_text,
    )
    new_flut.save()

def get_all_fluts():
    flut_list = models.Flut.objects.all()
    return flut_list

def get_ten_recent_fluts():
    flut_list = models.Flut.objects.all()

    flut_list_len = len(flut_list) + 1
    ten_less = int(flut_list_len - 10)

    return flut_list[ten_less:flut_list_len]

def get_all_fluts_for_user(user_name):
    return models.Flut.objects.filter(user_name=user_name)

def find_fluts_for_search(search_text):
    search_results = models.Flut.objects.filter(flut_text__contains=search_text)

    if len(search_results) < 10:
        return search_results

    else:
        search_results_len = len(search_results) + 1
        ten_less = int(search_results_len - 10)
        return ten_less
