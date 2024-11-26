n = int(input("Iveskite vienies ilgi (cm): "))
k = int(input("Iveskite vieno smugio gylis (cm): "))

smugiai = 0

while n > 0:
    smugiai += 1
    n -= k 

    if n < 0:
        n = 0

    print(f"Tuk! Smugis {smugiai}, liko ikalti {n} cm.")

print("Vinis ikalta")