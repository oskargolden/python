def first_name():
  userInput = input('Please Enter Your First Name: ')
  
  return  print(userInput)
    
def last_name():
  userInput = input('Please Enter Your Last Name: ')
  
  return  print(userInput)


keep_going = 'y'

while keep_going == 'y':

    first_last = input('Please Enter "first" or "last: "')

    if first_last == 'first':
        first_name()
    elif first_last == 'last':
        last_name()

    
    keep_going = input('Enter "y" to go again or "n" to exit')
    if keep_going != 'y':
        print('Goodbye')
