#Global Statement: If inside of a function you want to change the value of 
# a variable defined at the top level, then you have to tell Python that the 
# variable is not local. You do this with the global statement:
x = 50
def funk():
    global x
    print(f'x is: {x}')
    x = 2
    print(f'x changed locally to: {x}')
funk()
print(f'Value of x at the top level is still: {x}')

