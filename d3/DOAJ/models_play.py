from django.db import models


class Field(models.Model):
    name = models.TextField(defult='This is a Field Name')

    def __str__:
        return self.name

class Journal(models.Model):
    name = models.TextField(default='This is a Journal Title')
    field = models.ForeignKey(Field)

    def __str__:
        return self.name

class KeyWord(models.Model):
    name = models.TextField(default='This is a Keyword')
    journal = models.ForeignKey(Journal)

    def __str__:
        return self.name

class Article(models.Model):
    name = models.TextField(default='This is a Keyword')
    journal = models.ForeignKey(Journal)
    keyword = models.ForeignKey(Keyword)

    def __str__:
        return self.name
