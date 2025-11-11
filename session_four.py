###############  Tuples  ####################

# mytuple = ("apple", "banana", "cherry", "apple")
# print(mytuple[1])
# print(mytuple[:2])
# print(len(mytuple))
# print(mytuple.count("apple"))

###############   Sets  ##################

# myset = {"apple", "banana", "cherry", "apple"}
# print(myset)
# print (len(myset))
# myset.add('orange')
# print(myset)
# myset.remove("kewy")
# myset.remove('banana')
# print(myset)
# myset.pop()
# print(myset)
# del myset
# print(myset)
# myset2 = {"apple", "orange", "kewi"}
# print(myset2)
# print(myset.difference(myset2))
# print(myset.union(myset2))

############## Dictionary ###################

mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mydict["brand"])
print(mydict.get("year"))
print(mydict.keys())
print(mydict.values())
print(mydict.items())
mydict['engine'] = '1600cc'
print(mydict)
mydict.pop('model')
print(mydict)
mydict.popitem()
print(mydict)