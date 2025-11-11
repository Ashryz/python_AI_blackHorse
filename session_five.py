############### IF #######################
# a = 200
# b = 100
# if b > a:
#   print("b is greater than a")
# elif b < a:
#     print("b is less than a")
# else:
#    print ("b is equal a")

# x = int(input("Enter number: "))
# if x%2 == 0:
#    print("Even")
# else:
#    print("Odd")

# score = int(input("Enter your score: "))

# if score >= 90:
#     print("Grade: A")
# elif score >= 80 or score < 90:
#     print("Grade: B")
# elif score >= 70 or score < 80:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Fail")

# x = 41

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")
############### For ######################

# for x in "banana":
#   print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == 'banana': 
#         break
#     print(x)
# for x in fruits:
#     if x == 'banana': 
#         continue
#     print(x)
# for x in range(101):
#     if x%2 != 0 :
#         print(x)
numbers = [2,3,8]
product = 1 
for x in numbers:
    product = product * x 
print(f"product of nums : {product}")
