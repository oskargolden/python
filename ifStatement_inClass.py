print( '''
PLEASE ENTER TWO NUMBERS
''')

num1 = int(input('Please enter the first number: '))

num2 = int(input('Please enter the second number: '))

if num1 > num2:
    print('your first number', [num1], 'is larger then', [num2])
elif num1 < num2:
    print('Your second number',[num2], 'is larger then',[num1])
else:
    print('Your numbers are the same size')

           
