import random

while True:
    n = int(input("Iveskite teigiama sveika skaiviu n (didziausia reiksme, pvz., 100): "))

    if n <= 0: 
        print("Ivestas skaicius turi buti teigiamas! Bandykite dar karta.")
        continue

    atsitiktinis_skaicius = random.randint(1, n)
    print(f"Sugeneruotas atsitiktinis skaicius yra tarp 1 ir {n}. Spėkite jį!")

    spejimu_skaicius = 0
    netinkami_spejimai = 0 

    while True: 
        spejimas = int(input("Iveskite savo spejima: "))
        if spejimas < 1 or spejimas > n:
            print(f"Skaicius turi buti tarp 1 ir {n}. Bandykite dar karta.")
            netinkami_spejimai += 1
            continue 
        
        spejimu_skaicius += 1
        if spejimas < atsitiktinis_skaicius:
            print(f"Sugeneruotas skaicius yra DIDESNIS uz {spejimas}. Bandykite dar karta.")
        elif spejimas > atsitiktinis_skaicius:
            print(f"Sugeneruotas skaicius yra MAZESNIS uz {spejimas}. Bandykite dar karta.")
        else: 
            print(f"Teisingai! sugeneruotas skaicius buvo {atsitiktinis_skaicius}.")
            print(f"Jus atspejote per {spejimu_skaicius} bandymus (netinkamu ivedimu: {netinkami_spejimai}).")
            break

    zaisti_dar_karta = input("Ar norite zaisti dar karta? (taip/ne): ").lower()
    if zaisti_dar_karta != "taip":
        print("Aciu, kad zaidete! Iki!")
    break
