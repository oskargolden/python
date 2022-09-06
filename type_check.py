num = 1

string = 'string'

userI = input('please enter something')

if type(userI) == type(string):
    print(string)
elif type(userI) == type(num):
    print(type(num))
else:
    print('fail')

#use try except exception handeling for type check 
