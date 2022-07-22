number = [1,2,3,4,5,6]
even = []
for i in number:
    if i % 2 == 0:
        even.append(i)

print(even)

#####comprehension way
numbers = [11,12,13,14,15,16]
even2 = [i for i in numbers if i%2==0]
print(even2)
##
squ = [i*i for i in number if i%2==0]
print(squ)

####set unordered collection of unique items

s = set([1,2,3,4,5,2,3])
print(s)

###Dictionaries
cities = ['Delhi','paris','London']
countries = ['India','france','UK']
z = zip(cities,countries)
print(z)
for a in z:
    print(a)

d = {city:country for city, country in zip(cities,countries)}
print(d)