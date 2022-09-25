num = 1

string = 'string'



#if type(userI) == type(string):
   # print(string)
#elif type(userI) == type(num):
  #  print(type(num))
#else:
  #  print('fail')

#use try except exception handeling for type check 

try:
    userI = int(input('please enter something'))
except:
    print('please only enter numbers')
    userI = int(input('please enter something'))
    
