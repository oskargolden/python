#Write a program that calculates the total cost of a meal at a restaurant.

#The program should ask the user to enter the charge for the food,
#then calculate the amounts of an 18 percent tip and 7 percent sales tax. 

#Print each of these values and the total.

mealBill = float(input('how much was your dinner?'))

mealTip = mealBill * .18

mealTax = mealBill * .07

total = mealBill + mealTax + mealTip

print('the tax at 7%  is:$',round(mealTax, 2))

print('the tip at 18% equaled :$',round(mealTip, 2))

print('the total cost of your meal:$',round(total, 2))


newTip = input('would you like to add to the tip?: ')

newTipType = type(newTip)

if newTipType == str:
    newTip = input('would you like to add to the tip? (numbers only please): ')
    
if float(newTip) <= 1:
 print('Thank you! Your new total is:$',round(total + float(newTip),2) )
else:
 print('Have a good evening')


    


#if newTip == mealTip:
    

    

