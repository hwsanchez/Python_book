#Obvious:  + Plus, - Minus, * Multiply, / Divide

# ** (Power): 3 ** 4 gives 81 (z:B. 3 * 3 * 3 * 3 )

# // (Divide and floor): divides x by y AND round the answer DOWN to the nearest integer

# % (Modulo): Returns the remainder of the division:13 % 3 gives 1

#Guess the Number!

number = 25
guess = int(input('Enter a number: '))

if guess == number:
    print("You got it!!!")
elif guess < number:
    print("Sorry, it's a bit higher than that!")
else:
    print("No, it's a bit lower than that!")
print("Done!")

 
