
number = 0

while number < 100:
    number = int(input('Please Enter A Number Below 100 to Continue'))

for hello in range(42):
  print('Hello World')

sum = 0
userNum = 0
i =0
numberArr = ['First','Second','Third','Fourth','Fifth']

while i < 5:
    userNum = int(input(f'Please Enter Your {numberArr[i]} Number:  '))
    sum+= userNum
    i+=1

print(sum,'is the total of your numbers')


colours = ['Blue','Orange','Magenta','White']

for color in colours:
    print(color)
