# Convert distant given in feet and inches into meter and centimeter.
print('feet and inches into meter and centimeter  Converter.')
f=int(input('Enter distance in feet: '))
i=int(input('Enter distance in inches: '))

dis= f*12 + i                  #Convert feet and inches ---> inches
dist= dis*(2.54)           #Convert inches ---> centimetres
metres= dist//100
cm= dist%100
print(f'{f} feet and {i} inches     =    {metres} meter and {cm} centimeters.')