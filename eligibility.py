Height=int(input('What\'s your Height?'))
if(Height>=3):
    age=int(input('what\'s your age?'))
    if(age>=18 and age<=70):
        print('Please pay 250/-')
    elif(age>=10 and age<18):
        print('Please pay 150/-')
    else:
        print('Sorry! You cannot ride')
else:
    print('Sorry! You cannot ride')
print('Thank you!')