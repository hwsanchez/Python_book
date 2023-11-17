#Return Statement: is used to return FROM a function i.e. break out of the function.

def maximum(x, y):
    '''Prints the maximum of two numbers.


    The two values must be integers

    You are in help() Press: 'q'  to quit!'''
    x = int(x)
    y = int(y)

    if x > y:
        return x 
    elif x == y:
        return 'The numbers are equal cara-e-peo!'
    else:
        return y

x = input('type number x:')
y = input('type numbe y:')
print(maximum(x, y))
print(maximum.__doc__)
help(maximum)

