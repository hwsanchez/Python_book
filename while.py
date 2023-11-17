# j: line up
# k: line down
# h: left
# l: right
# :set mouse=a (Activates the mouse!)
# :set relativenumber
# to open the .vimrc file from the promt: $vim ~/.vimrc 

number = 25
running = True
while running:
    guess = int(input('Enter a number : '))
    if guess == number:
        print("You've got it Meng!!!")
        running = False
    elif guess < number:
        print('a bit higher...')
    else:
        print('a bit lower...')
else: #this else belongs to the while loop!
    print('GAME OVER!')
