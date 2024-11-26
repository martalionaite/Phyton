kiekis = 0

for skaicius in range(1000, 10000):
    kaire = skaicius // 100
    desine = skaicius % 100

    if (kaire + desine) ** 2 == skaicius: 
        print(skaicius)
        kiekis += 1

print(f"Kiekis: {kiekis}")