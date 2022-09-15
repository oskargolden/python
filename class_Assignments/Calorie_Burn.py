#Running on a particular treadmill you burn 4.2 calories per minute.

#Write a program that uses a for loop to display the number of calories burned
#after 10, 15, 20, 25 and 30 minutes.

burn = 4.2
calories = 0

minute = 0
second = minute /60
hour = minute * 60






for min in range(31):
    calories+=burn
    minute+=1
    if minute == 10:
        print(f'You have been running for {min+1} minutes and you have burned calories {round(calories,2)}')
    elif minute == 15:
        print(f'You have been running for {min+1} minutes and you have burned calories {round(calories,2)}')
    elif minute == 20:
        print(f'You have been running for {min+1} minutes and you have burned calories {round(calories,2)}')
    elif minute == 25:
        print(f'You have been running for {min+1} minutes and you have burned calories {round(calories,2)}')
    elif minute == 30:
        print(f'You have been running for {min+1} minutes and you have burned calories {round(calories,2)}')

for min in range(31):
    calories+=burn
    minute+=1
    if minute > 9 and minute % 5==0:
        print(f'You have been running for {min+1} minutes and you have burned calories {round(calories,2)}')
