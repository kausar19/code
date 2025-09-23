#take name input from the user 
name = ("kausar")

#reverse the name using slicing
reversed_name = name[::-1]

#print the reversed name
print("reversed name: ", reversed_name)

#take name input from the user 
#name = input("Enter your name: ")

#reverse the name using slicing
#reversed_name = name[::-1]

#print the reversed name
#print("Reversed name:", reversed_name)


name = "kausar"
reversed_name = " "
#loop through each character from the end
for char in name:
    reversed_name = char + reversed_name
    print("reversed name :", reversed_name)
