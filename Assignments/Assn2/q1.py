# Convert the time entered in hh,min and sec into seconds.
print('Convert the time entered in hh,min and sec into seconds.')
hr=int(input('Enter number of hours: '))
min=int(input('Enter number of minutes: '))
sec=int(input('Enter number of seconds: '))
time=hr*3600+min*60+sec
print(f'{hr} hours,{min} minutes,{sec} seconds is equal to {time} seconds in total.')