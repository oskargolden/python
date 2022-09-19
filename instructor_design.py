command =""
catcount=0
dogcount=0
othercount=0

while command != 'stop':
    command = input('what type of animal came in?')
    print('Animal: ', command)

    if command == 'cat':
        print('you saw a cat')
        catcount+=1
    elif command == 'dog':
        print('you saw a dog')
        dogcount+=1
    elif command != 'stop':
        print('you saw some other kind of animal ', command)
        othercount+=1

              
print('Cats: ', catcount, 'Dogs: ', dogcount, 'Other: ', othercount)
