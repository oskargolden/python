daynum=input("give me a day number between 1 and 7 to convert: ")

daynum=int(daynum)

dayname=""

if daynum==1:
     dayname='Sunday'
elif daynum==2:
     dayname='Monday'
elif daynum==3:
     dayname='Tuesday'
elif daynum==4:
     dayname='Wednesday'
elif daynum==5:
     dayname='Thursday'
elif daynum==6:
     dayname='Friday'
elif daynum==7:
     dayname='Saturday'
else:
    dayname="Error"

print("The day for", daynum, "is", dayname)

      
