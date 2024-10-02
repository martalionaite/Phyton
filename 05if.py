sk = int(input('sk ='))
laimingas = (sk >= 5 and sk <= 10) or (sk > 20 and sk <= 25)
if laimingas : 
    print('Skaicius laimingas')
else:
    print('Skaicius nelaimingas')