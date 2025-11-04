# ################ slicing with step ###########################
# x = 'Hello, World!'
# print(x[::2])       #-> Hlo ol!
# print(x[:10:3])     #-> Hl r
# print(x[-5:-2])     #-> orl
# print(x[-10:-2])    #-> lo, Worl
# print(x[-10:-2:2])  #-> l,Wr

# ################ string format ###########################
# age = 20 
# text = f'this is my age {age}'
# print(text)
# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)
# txt_op = f"The price is {price * 2} dollars"
# print(txt_op)

# x = int(input('Enter num1: '))
# y = int(input('Enter num2: '))
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x//y)
# print(x%y)
# print(x**y)

################ data structure ###########################
test_list = [1,1,3,2,5,4]
print(test_list)
print(type(test_list))
print(len(test_list))
test_list[0] = 'access'
print(test_list)
print(test_list[2:])   
test_list.insert(2,'insert')
print(test_list)
test_list.append('append')
print(test_list)
test_list.extend([1,2,3])
print(test_list)
test_list.remove('access')
print(test_list)
test_list.pop(1)    # if u do not add index to pop it will remove last one
