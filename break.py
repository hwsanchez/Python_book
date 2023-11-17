while True:
    s = input('Enter a phrase or a word(type\'quit\' to end: ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too short meng!')
        continue
    print('Length of the string is', len(s))
print('Done!')
