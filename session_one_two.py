print("Hello From Python & AI course !")
print("""Hello
From
Python
&
AI
Course
!""")
###################### Variables ##########################
greeting = 'Hello From Python & AI course !'
print(greeting)
x = 5 
y = 10 
print(x)
x = x -1
print(x)
print(y)
y = y+x
print(y)
# assign multiple values
x = y = z = "Orange"
print(x)
print(y)
print(z)
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# index of string
print(x[1])
print(x[0],x[1])
print(x[0:2])                    #slicing return [start: end] and end not included
print(x[-1])                     #return the last char
print(x[1:])                     #retun from start to the end of string
print(x.replace('r','t'))        #return new string with replaced old char_with new_char
sentence =  x + y                #return new string concated from x and y 
print(sentence)
print(sentence.split(' ')[0])    #return the first word after split the string 
print(sentence.split('n'))       #return list of splited words 
print(sentence.split('n')[1])    # retun the second word after split
############################################################################