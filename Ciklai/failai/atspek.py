import random

def zaidimas():
    print("Sveiki atvykę į skaičių spėjimo žaidimą!")

    while True:
        try:
            n = int(input("Įveskite didžiausią skaičių, kuris gali būti sugeneruotas (teigiamas sveikas skaičius): "))
            if n <= 0:
                print("Skaičius turi būti teigiamas! Bandykite dar kartą.")
                continue
            break
        except ValueError:
            print("Įveskite sveiką skaičių!")

    sugeneruotas = random.randint(1, n)
    print(f"Atsitiktinis skaičius buvo sugeneruotas tarp 1 ir {n}. Bandykite jį atspėti!")

    spejimu_sk = 0 

    while True:
        try:
            spejimas = int(input("Įveskite savo spėjimą: "))
            if spejimas <= 0:
                print("Įveskite teigiamą skaičių!")
                continue
            spejimu_sk += 1 

            if spejimas < sugeneruotas:
                print("Sugeneruotas skaičius didesnis! Bandykite dar kartą.")
            elif spejimas > sugeneruotas:
                print("Sugeneruotas skaičius mažesnis! Bandykite dar kartą.")
            else:
                print(f"Teisingai! Sugeneruotas skaičius buvo {sugeneruotas}. Jūs atspėjote per {spejimu_sk} spėjimus.")
                break
        except ValueError:
            print("Įveskite sveiką skaičių!")


    dar_karta = input("Ar norite žaisti dar kartą? (taip/ne): ").lower()
    if dar_karta == "taip":
        zaidimas()  
    else:
        print("Ačiū, kad žaidėte!")

zaidimas()
