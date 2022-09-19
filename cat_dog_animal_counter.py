cats = 0
dogs=0
other=0
going='going'
runningList = []

while going != 'stop':
    animal = input('what animal are you recieveing: ')
    if animal == 'cat':
        cats+=1
    elif animal =='dog':
        dogs+=1
    else:
        other+=1
    runningList.insert(0, animal)

    going = input("""
Enter 'stop'. Otherwise press enter.

""")

if cats == dogs and dogs == other:
    print(f'Wow you saw the same number of cats [{cats}], [{dogs}] dogs, and [{other}] of whatever else comes through here')
elif cats > dogs:
    print(f'You saw {cats} cats, way more than any other animal ')
elif dogs > cats:
    print(f'You saw {dogs} dogs, way more than any other animal ')
else:
    print(f"You had {other} of I don't know what kinda animal.")
 
print('this is everything you entered: ', runningList)
