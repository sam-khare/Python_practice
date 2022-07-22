# book = {}
# book['tom']={
#     'name' : 'tom',
#     'address' : 'x road y city',
#     'phone' :  534789
# }
#
# book['jack']={
#     'name' : 'jack',
#     'address' : 'd road m city',
#     'phone' :  1563490
# }
#
# import json
# s = json.dumps(book)
# with open("C://Users//DELL-//Desktop//Sam_Py//pycharm//book.txt","w") as f:
#     f.write(s)

# f =  open("C://Users//DELL-//Desktop//Sam_Py//pycharm//book.txt","r")
# k = f.read()
# print(type(k))
#
# import json
# book = json.loads(k)
# print(type(book))
#
# for p in book:
#     print(book[p]['name'])

f = open("C://Users//DELL-//Desktop//Sam_Py//pycharm//book.txt","r")
for line in f:
    tokens=line.split(' ')
    print(len(tokens))
f.close()
