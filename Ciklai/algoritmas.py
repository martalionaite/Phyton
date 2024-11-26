x1 = int(input("Įveskite, kiek kilometrų automobilis nuvažiavo per pirmą valandą (x1): "))
y1 = int(input("Įveskite, kiek metrų automobili nuvažiavo per pirmą valandą (y1): "))

x2 = int(input("Įveskite, kiek kilometrų automobilis nuvažiavo per antrą valandą (x2): "))
y2 = int(input("Įveskie, kiek metrų automobili nuvažiavo per antrą valandą (y2): "))

bendri_kilometrai = x1 + x2
bendri_metrai = y1 + y2

if bendri_metrai >= 1000:
    papildomi_kilometrai = bendri_metrai // 1000
    bendri_kilometrai += papildomi_kilometrai
    bendri_metrai = bendri_metrai % 1000

print(f"Viso automobili nuvažiavo {bendri_kilometrai}km ir {bendri_metrai}m kelio.")