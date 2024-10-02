

#13. Programišius įsilaužė į kompiuterį ir pradėjo siųstis informaciją. Apsauginė programa, pastebėjusį
#nesankcionuotą prisijungimą, atjungė programišių po 2 sekundžių. Per pirmą sekundę jis pasisavino x1
#kilobaitus ir y1 baitus informacijos, o per antrą sekundę – x2 kilobaitus ir y2 baitus informacijos. Parašykite
#programą, nustatančią, kiek informacijos programišius parsisiuntė per 2 sekundes.
#Pasitikrinkite. Kai x1 = 15, y1 = 754, o x2 = 38, y2 = 954 turi būti spausdinama. 

x1 = int(input('Kiek kilobaitu pasisavino per pirma sek?...'))
y1 = int(input('Kiek baitu pasisavino per pirma sek?...'))
x2 = int(input('Kiek kilobaitu pasisavino per antra sek?...'))
y2 = int(input('Kiek baitu pasisavino per antra sek?...'))
visoBaitais = x1*1024 + y1 + x2*1024 + y2
kilobaitu = visoBaitais // 1024
baitu = visoBaitais % 1024
print(f'Programisius pavoge {kilobaitu}Kb {baitu}B informacijos')