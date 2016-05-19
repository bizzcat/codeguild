from django.db import models
from django.utils import timezone


# class User(models.Model):
#     user_name = models.TextField()
#
#     def __str__(self):
#         return self.user_name
#
#     # def __init__(self):
#     #     return 'User(user_name: {})'.format(self.user_name)


class Flut(models.Model):
    """docstring for Flut"""

    user_name = models.TextField(max_length=20, default='Flutter User')
    flut_text = models.TextField(max_length=140, default='Flitter flut flit fleet flot flippidy fleek fleeb, flibber flabber flip flop.')
    time_stamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '''{}
        {}
        {}
        {}
        '''.format(self.user_name, self.flut_text, self.time_stamp, self.id)
    #
    # def __init__(self):
    #     return 'Flut(User: {}, Text: {})'.format(self.user_name, self.flut_text)
