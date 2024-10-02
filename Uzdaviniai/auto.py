## Automobilis per pirma valanda nuvaziavo x1 km ir y2 m kelio kiek per antra valanda x2 kilomentru ir y2. Parasyti programa kuri apskaiciuos koki atstuma automobilis nuvaziuos per 2h.

# Pirmos valandos duomenys
x1 = int(input('Kiek automobilis nuvažiavo kilometrų per pirmą valandą:'))
y1 = int(input('Kiek automobilis nuvažiavo metrų per pirmą valandą:'))

# Antros valandos duomenys

x2 = int(input('Kiek automobilis nuvažiavo kilometrų per antrą valandą:'))
y2 = int(input('Kiek automobilis nuvažiavo metrų per antrą valandą: '))


total_kilometrai = x1 + x2
total_metrai = y1 + y2

if total_metrai >= 1000:
    extra_kilometrai = total_metrai // 1000
    total_kilometrai += extra_kilometrai
    total_metrai = total_metrai % 1000

print(f'Automobilis per 2 valandas {total_kilometrai} kilometrų ir {total_metrai} metrų')