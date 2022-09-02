bill_Pre_Tax = float (input('please enter the cost of your meal pre-tax: $'))

Rest_Tax = round(bill_Pre_Tax * .07, 2)

Tip = round(bill_Pre_Tax * .18, 2)

total = round(Tip + Rest_Tax + bill_Pre_Tax, 2)

print('The tax on your meal is:$', Rest_Tax)

print('The tip on the your meal is:$', Tip)

print('The total cost of your meal is:$', total)

newTip = input('would you like to add extra tip? enter y/n')

if newTip == 'y':
 newTip = float(input('Please enter the extra tip:$'))
 #DRY
 print('The staff appreciates your tip. your new total is: $', total + newTip)
elif newTip == 'n':
 print('We hope you enjoyed your evening :)')
else:
 newTip = float(input('would you like to add extra tip? enter y/n'))
 #DRY
 print('The staff appreciates your tip. your new total is: $', total + newTip)
