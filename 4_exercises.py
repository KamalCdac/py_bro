# Exercise 1 Rectangle Area Calc

length = float(input("Enter length of rectangle"))
width = float(input("Enter width of rectangle"))
area = length * width
print(f"the area is {area} cm")

# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is {total}")


#Madlibs game
# word game where you create a story by filling in blanks with random words

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
adjective3 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing")
print (f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print (f" {noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")