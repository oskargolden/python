burn = 4.2
calories = 0
minute = 0

for min in range(31):
    calories+=burn
    minute+=1
    if minute > 9 and minute % 5==0:
        print(f'You have been running for {min+1} minutes and you have burned calories {round(calories,1)}')

