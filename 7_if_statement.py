# if = Do some ccode only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))
if age >=100:
    print("You are too old to sign up!!")
elif age>=18:
    print("You are 18+ you are signed up!!")
elif age <0:
    print("You haven't been born yet!!")
else:
    print("You are under 18 years you are not signed up!!")

#----------------------------------------------------------

response = input("Would you like food? (Y/N): ")
if response == "Y":
    print("Have some food")
else:
    print("No food for you")

#-----------------------------------------------------------

name = input("Enter your name: ")
if name == "":
    print("You didn't type in your name")
else:
    print(f"Your name is {name}")

#-----------------------------------------------------------

for_sale = True
if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")