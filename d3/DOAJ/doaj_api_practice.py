import requests
import json
import math
from . import models

zzz_url = 'https://doaj.org/api/v1/search/articles/bibjson.subject.term%3Acomputer%20software?pageSize=100'

zzz = requests.get(zzz_url)

zzz_data = zzz.json()

total_articles = int(zzz_data['total'])
page_size = int(zzz_data['pageSize'])
total_pages = math.ceil(total_articles / page_size)
if total_pages > 4: total_pages = 4
the_data = []
articles = []


i = 1
while i <= total_pages:
    url = 'https://doaj.org/api/v1/search/articles/bibjson.subject.term%3Acomputer%20software?pageSize=100&page={}'.format(i)
    r = requests.get(url)
    data = r.json()
    for article in data['results'][0:]:
        if 'EN' in article['bibjson']['journal']['language']:
            if 'keywords' in article['bibjson']:
                if 'subject' in article['bibjson']:
                    if 'title' in article['bibjson']:
                        articles.append(article)
    i += 1

keywords = []
journals = []
journals_to_articles = {}
kw_to_articles = {}
journal_kw_article = {}

for article in articles:
    journal_title = article['bibjson']['journal']['title']
    journals.append(journal_title)

for journal in journals:
    journal_kws = []
    for article in articles:
        if article['bibjson']['journal']['title'] == journal:
            article_kws = article['bibjson']['keywords']
            for kw in article_kws:
                journal_kws.append(kw)

    for kw in journal_kws:
        kw_to_articles[kw] = []
        for article in articles:
            if article['bibjson']['journal']['title'] == journal:
                if kw in article['bibjson']['keywords']:


                    article_name = article['bibjson']['title']
                    article_kws = article['bibjson']['keywords']
                    article_year = article['created_date'][0:4]
                    article_id = article['id']
                    article_url = article['bibjson']['link'][0]['url']

                    # the_article = {'title': article_name, 'kws': article_kws, 'year': article_year, 'id': article_id, 'url': article_url}

                    kw_to_articles[kw].append(the_article)

        journal_kw_article[journal] = kw_to_articles


a=1
b=1
c=1

# >>> fruit = Fruit.objects.create(name='Apple')
# >>> fruit.name = 'Pear'
# >>> fruit.save()
# >>> Fruit.objects.values_list('name', flat=True)

field = 'Computer Software'

f1 = models.Field(field)

for z in journal_kw_article:
    journal_object = 'j' + str(a)
    journal_object = models.Journal(name=z, field=f1)
    a+=1
    print(journal_object)
    # print(z)

    for kw in journal_kw_article[z]:
        keyword_object = 'kw' + str(b)
        keyword_object = models.Keyword(name=kw, journal=journal_object)
        b += 1
        print("\t" + journal_object)
        # print("\n\t" + kw)

        for article in journal_kw_article[z][kw]:
            article_object = 'a' + c
            article_object = models.Article(name=article['title'], year=article['year'], url=article['url'], keyword=keyword_object, journal=journal_object)
            c += 1
            print("\t\t" + article_object)


    # print('\n\n\n')

print(journal_kw_article)

the_article = {'title': article_name, 'kws': article_kws, 'year': article_year, 'id': article_id, 'url': article_url}












#
# for (var journal in dataDict) {
#   id_dict[jnum.toString()] = journal
#   jLen += 1
#   // console.log('journal' + jnum + '||' + journal)
#   jnum += 1
#
#   for (var kw in dataDict[journal]) {
#     id_dict[jnum.toString()] = kw
#     kLen += 1
#     jnum += 1
#
#     for (var article in dataDict[journal][kw]) {
#       id_dict[jnum.toString()] = dataDict[journal][kw][article]['title']
#       aLen += 1
#       // console.log('article' + jnum + '||' + dataDict[journal][kw][article]['title'])
#       jnum += 1
#
#     }
#   }
# }








#
#
#             journals_to_articles[journal_title] = the_article
#
#
#
#
#
#
#
#
#
#
#
# subjects = []
# journals = {}
# subject_to_journal_title = {}
# keyword_to_articles = {}
#
#
# # for result in the_data:
# #     for article in result:
# #         first_articles.append(article)
# #
# # for article in first_articles:
# #     if 'EN' in article['bibjson']['journal']['language']:
# #         if 'keywords' in article['bibjson']:
# #             if 'subject' in article['bibjson']:
# #                 if 'title' in article['bibjson']:
# #                     articles.append(article)
#
# for article in articles:
#     subject = article['bibjson']['subject'][0]['term']
#     if subject not in subjects:
#         subjects.append(subject)
#
#
# for subject in subjects:
#     subject_to_journal_title[subject] = []
#     for article in articles:
#         if subject in article['bibjson']['subject'][0]['term']:
#             journal_title = article['bibjson']['journal']['title']
#             if journal_title not in subject_to_journal_title[subject]:
#                 subject_to_journal_title[subject].append(journal_title)
#
#
# for subject in subjects:
#     for journal_title in subject_to_journal_title[subject]:
#
#         for article in articles:
#             if journal_title == article['bibjson']['journal']['title']:
#                 journal_title = {'jrnl': journal_title, 'kws': article['bibjson']['keywords']}
#
#         for keyword in journal_title['kws']:
#             keyword_to_articles[keyword] = []
#             for article in articles:
#                 if journal_title['jrnl'] == article['bibjson']['journal']['title']:
#                     if keyword in article['bibjson']['keywords']:
#                         article_name = article['bibjson']['title']
#                         article_date = article['created_date']
#                         article_id = article['id']
#
#                         the_article = {'title': article_name, 'date': article_date, 'id': article_id}
#                         keyword_to_articles[keyword].append(the_article)
#             keyword = keyword_to_articles[keyword]
#
#
# for z in keyword_to_articles:
#     print(z)
#     print(keyword_to_articles[z])
#     print("\n")
#
# # print(keyword_to_articles)
# print("\n\n\n\n")
# print(subject_to_journal_title)





# for subject in subjects:
#     for journal_title in subject_to_journal_title[subject]:
#         for keyword in journal_title['kws']:
#             keyword_to_article = []
#             for article in articles:
#                 if journal_title['jrnl'] == article['bibjson']['journal']['title']:
#                     if keyword in article['bibjson']['keywords']:
#                         article_name = article['bibjson']['title']
#                         article_date = article['created_date']
#
#                         the_article = {'title': article_name, 'date': article_date}
#                         keyword_to_article[keyword].append(the_article)


#                     keyword = {'kw': keyword, 'artcls': }
#
#
#
#
#
#
# big_dict = {'dmn': 'Data', 'data': second_level_dict}
#
#
# x=0
#
#         if 'EN' in article['bibjson']['journal']['language']:
#             if 'keywords' in article['bibjson']:
#                 if 'subject' in article['bibjson']:
#                     if 'title' in article['bibjson']:
#
#                         print('\n\n\n\n\n************************************************************ARTICLE {}************************************************************'.format(x))
#
#
#
#
#                         print("\nJournal Title: {}".format(article['bibjson']['journal']['title']))
#
#                         print("\nArticle Title: {}".format(article['bibjson']['title']))
#
#                         print("\nLanguage: {} \n".format(article['bibjson']['journal']['language']))
#
#                         if 'keywords' not in article['bibjson']:
#                             article['bibjson']['keywords'] = ['No Keywords']
#
#                         else:
#                             for keyword in article['bibjson']['keywords']:
#                                 print(('\tKeyword: {}').format(keyword))
#
#                         print("\nSubject Term: {} \n".format(article['bibjson']['subject'][0]['term']))
#
#                         x += 1



# {
#   "pageSize": 0,
#   "timestamp": "string",
#   "results": [
#     {
#       "last_updated": "string",
#       "id": "string",
#       "bibjson": {
#         "start_page": 0,
#         "title": "string",
#         "journal": {
#           "publisher": "string",
#           "license": [
#             {
#               "url": "string",
#               "type": "string",
#               "title": "string"
#             }
#           ],
#           "language": [
#             "string"
#           ],
#           "title": "string",
#           "country": "string",
#           "number": "string",
#           "volume": "string"
#         },
#         "author": [
#           {
#             "affiliation": "string",
#             "email": "string",
#             "name": "string"
#           }
#         ],
#         "subject": [
#           {
#             "code": "string",
#             "term": "string",
#             "scheme": "string"
#           }
#         ],
#         "month": "string",
#         "link": [
#           {
#             "url": "string",
#             "type": "string",
#             "content_type": "string"
#           }
#         ],
#         "year": "string",
#         "keywords": [
#           "string"
#         ],
#         "identifier": [
#           {
#             "type": "string",
#             "id": "string"
#           }
#         ],
#         "abstract": "string",
#         "end_page": "string"
#       },
#       "created_date": "string"
#     }
#   ],
#   "query": "string",
#   "total": 0,
#   "page": 0
# }
