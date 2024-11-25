boyfriend = str(input("Enter boyfriend's name:"))
girlfriend = str(input("Enter girlfriend's name:"))
bf=boyfriend.lower()
gf=girlfriend.lower()
a=(bf.count('t')+bf.count('r')+bf.count('u')+bf.count('e')+bf.count('l')+bf.count('o')+bf.count('v')+bf.count('e'))
b=(gf.count('t')+gf.count('r')+gf.count('u')+gf.count('e')+gf.count('l')+gf.count('o')+gf.count('v')+gf.count('e'))
love_count = str(a) + str(b)
print(f"love count is {a}{b}%")
if int(love_count) < 10:
    print("Keep going")
elif int(love_count)>40 and int(love_count)<70:
    print("Love count is between 40 to 70")
else:
    print("Too much love")