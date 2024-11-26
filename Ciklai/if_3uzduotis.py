a = float(input("Įveskite pirmą kraštinę (a): "))
b = float(input("Įveskite pirmą kraštinę (b): "))
c = float(input("Įveskite pirmą kraštinę (c): "))

plotas1 = a * b
plotas2 = a * c
plotas3 = b * c

maziausias_plotas = min(plotas1, plotas2, plotas3)

print(f"Maziausias staciakampio plotas yra: {maziausias_plotas}")
