#VarArgs parameters: sometimes you want to define functions that take ANY number of parameters.
#this is achieved using stars: *

def total(a=5, *numbers, **phonebook):
    print(f'a: {a}')

    #iterate thoriugh all items in tuple
    for item in numbers:
        print(f'Item: {item}')
    else:
        print('End of Item iteration!')

    #iterate through all items in dictionary
    for name, number in phonebook.items():
        print(name, number)
    else:
        print(f'End of dictionary iteration!')

total(1,2,3,4,5,6,Pepe=22354444,Juan=4443323,Arakatriskiti=5558987)
