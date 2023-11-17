#Default Argument Values: for some functions, you might want to 
# make some parameters OPTIONAL and use default values
# in case the user do not want to provide them:
di = 'Que hubo'
def say(message, name='user'):
    print(message, name)
say('Hello', 'Pargete')
say('Hello')
say(di, 'Careverga!')
