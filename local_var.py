#Local Variables:
x = 50

def funk(x):
    print(f'x is:  {x}')
    x = 2 
    print(f'Just changed local x to: {x}')
funk(x)
print(f'Outsinde of the function x is: {x}')
