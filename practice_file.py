#backup classes for practice
#arrays
tiffin = ["roti", "sabji", "dal", "rice", "curd"]
print(tiffin[0])
print(tiffin[0-4])

#arithmetic operators
#all math symbols
a = 10 
b = 3
print(a + b)
print(a % b)
print(a - b)
print(a * b)

#logical operators
#and, or , not
#age >10
#height >130cm
age = int(input("17"))
height = int(input("150cm"))
if age > 10 and height > 130:
    print("you can enjoy the ride!")
else:
    print("you can't go on the ride.")

#or example
is_student = True
is_member = False
if is_student or is_member:
    print("you get a discount")
else:
    print( "you don't get a discount")
    #not example
    today = input("whatr day is today?")
    if not today == "sunday":
        print("go to school")
    else:
        print("enjoy your day off!")

