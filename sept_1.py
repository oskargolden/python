#Average finder
s1 = 75

s2 = 67

s3 = 85

print(s1)
print(s2)
print(s3)

total = s1 + s2 + s3

print('Average Score: ', round(total/3,2))

#MPG finder

miles = int(input('Enter Miles: '))

gallons = int(input('Enter gallons: '))

mpg = miles/gallons

print('Your MPG is :',mpg)

print('please enter two numbers')

userNumb = float(input('please enter a number: '))

if userNumb < 0:
    print('you entered a negative number ', userNumb)
elif userNumb > 0:
    print('You entered a positive number', userNumb)


print('You entered: ', userNumb)


#number size finder 

num1 = int(input('please enter the first number: '))

num2 = int(input('please enter the second number: '))

if num1 > num2:
    print('your first number is larger')
elif num1 < num2:
    print('your second number is larger')
else:
    print('your numbers are the same size')

           

