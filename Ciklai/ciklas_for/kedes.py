n = int(input("Įveskite eilių skaičių (n): "))
k = int(input("Įveskite kėdžių skaičių pirmoje eilėje (k): "))

suma_kedziu = 0

for eile in range(1, n + 1):
    kedziu_sk = k + (eile - 1) * 2
    suma_kedziu += kedziu_sk

print(f"Reikia užsakyti s = {suma_kedziu} kėdžių.")