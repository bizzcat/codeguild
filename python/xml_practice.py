import xml.etree.ElementTree as etree
from urllib.request import urlopen
import xmltodict



def homepage():
    file = urlopen("http://www.w3schools.com/xml/simple.xml")
    data = xmltodict.parse(file.read())
    return data

data = homepage()

# print(data['breakfast_menu']['food'][0]['name'])
#
# print(data['food'])

i = 0
for x in data:
    print(x) # breakfast_menu
    for y in data[x]:
        print("\t" + y) # food
        while i < len(data[x][y]):
            for v in data[x][y][i]:
                print("\t\t" + v) # name, price, descript
                print("\t\t\t" + str(data[x][y][i][v])) # values of above
            i += 1





# breakfast_menu
#     food
#         name
#         price
#         descript
#         calories
#
#     food
#         ...
#
#     ...

#
# tree1 = etree.parse("http://www.w3schools.com/xml/simple.xml")
# print("tree1", tree1)
#
# xml_file = urlopen("http://www.w3schools.com/xml/simple.xml")
# print("xml_file", xml_file)
#
# data = xml_file.read()
#
# tree1 = etree.parse("http://www.w3schools.com/xml/simple.xml")
# print("tree1", tree1)

#
# data = xml_file.read()
# print("data", data)
#
# data2 = xmltodict.parse(data)
# print("data2", data2)
#
# tree = etree.parse(data)
# print("tree", tree)


