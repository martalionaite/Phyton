import random

def lazdeliu_zaidimas():
    print("Sveiki atvykę į lazdelių žaidimą!")

    lazdeliu_skaicius = 10

    zaidejas1 = input("Įveskite pirmo žaidėjo vardą: ")
    zaidejas2 = input("Įveskite antro žaidėjo vardą: ")

    zaidejas = random.choice([zaidejas1, zaidejas2])
    print(f"Žaidimą pradeda {zaidejas}!")

    while lazdeliu_skaicius > 0:
        print(f"Liko {lazdeliu_skaicius} lazdelių.")

        while True:
            try:
                kiek_paima = int(input(f"{zaidejas}, kiek lazdelių norite paimti (1-3)? "))
                if 1 <= kiek_paima <= min(3, lazdeliu_skaicius):
                    break
                print(f"Galite paimti tik nuo 1 iki {min(3, lazdeliu_skaicius)} lazdelių.")
            except ValueError:
                print("Įveskite sveiką skaičių nuo 1 iki 3.")

        lazdeliu_skaicius -= kiek_paima

        if lazdeliu_skaicius == 0:
            print(f"Lazdelės baigėsi! {zaidejas} pralaimėjo!")
            break

        zaidejas = zaidejas1 if zaidejas == zaidejas2 else zaidejas2

    dar_karta = input("Ar norite žaisti dar kartą? (taip/ne): ").lower()
    if dar_karta == "taip":
        lazdeliu_zaidimas()
    else:
        print("Ačiū, kad žaidėte!")

lazdeliu_zaidimas()
