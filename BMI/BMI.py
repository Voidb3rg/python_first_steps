#!/usr/bin/python
''' main '''

name=input('Name:')
print('Hallo',name)
groesse=input('Körpergröße:')

bmi=0
while True:
    gewicht=input('Gewicht:')
    if not gewicht:
        break
        bmi=round(int(gewicht)/(float(groesse)**2),2)
        continue
    print('BMI:',bmi)
    if bmi >= 25:
        print(name,', du hast Übergewicht')
    elif bmi <=18.5:
        print (name,', du hast Untergewicht')
    else:
        print(name,', du hast Normalgewicht')
        
print ('Ende des Programms')

print ('jetzt aber wirklich')
