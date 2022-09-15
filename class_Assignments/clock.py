time = 0

burn = 4.2
calories = 0
minute = 9
second=0

while minute < 31:
    for hours in range(24):
        for minutes in range(60):
            calories+=burn
            for seconds in range(60):
               second+=1
               if second % 60 == 0:
                   minute+=1
               elif second % 60 == 0 and minute > 9 and minute % 5==0:
                    print('calories count', calories)
               else:
                    print(minute)
                    print(seconds)
             

                    
                
                
