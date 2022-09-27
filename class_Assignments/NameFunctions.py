def names(name):
  return  name
    


print('''

Please Enter "first" or "last".

Enter "print" When You Would Like To See Names Entered

''')

keep_going = 0 
while keep_going < 1:
    userInput = input(':  ')
    if userInput == 'first':
        fname = input('Please Enter Your First Name: ')
    elif userInput == 'last':
        lname = input('Please Enter Your Last Name: ')
    elif userInput == 'print':
       print(names(fname), names(lname))
    keep_going = int(input('Enter 0 To Enter More Commands or Enter 1 To Exit: '))
    if keep_going > 0:
        print('Goodbye',names(fname), names(lname) )
