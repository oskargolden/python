states = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia","DC", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

winnings = int(input('Please enter winnings: '))

purchase_state = input('Please enter state in which ticket was purchased: ')
resident_state = input('Do you live in that state? Enter y/n')

if resident_state == 'n':
    resident_state = input('Please enter the state you live in: ')
    
    print(resident_state)
elif resident_state == 'y':
    print('Thats a nice place to live')


if winnings <= 5000:
    payout = winnings
elif winnings >= 5000:
    payout = winnings - (winnings * .24)




print(payout)
