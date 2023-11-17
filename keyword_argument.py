#Keyword Argument: You can give values to some arguments by naming them in the function call:
def funk(a, b=5, c=10):
    print(f'a is {a}, and b is {b}, and c is {c}')
funk(3, 7)
funk(25, c=24)
funk(c=50, a=100)
funk(1,2,3)

