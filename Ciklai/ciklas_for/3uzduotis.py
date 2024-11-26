n = int(input("Iveskite paskutinio nario septynetu skaiciu: "))

eilutes_suma = 0
dabartinis_narys = 0

for i in range(1, n + 1):
    dabartinis_narys = dabartinis_narys * 10 + 7
    eilutes_suma += dabartinis_narys

print(f"Simpatiskosios eilutes suma: {eilutes_suma}")