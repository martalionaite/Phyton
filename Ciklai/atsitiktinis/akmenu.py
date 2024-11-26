import random

akmenu_skaicius = random.randint(15, 30)
print(f"Pradėkime žaidimą! Maiše yra {akmenu_skaicius} akmenys.")

while akmenu_skaicius > 0:
    while True:
        try:
            vartotojo_akmenys = int(input("Įveskite, kiek akmenų norite paimti (1-3): "))
            if 1 <= vartotojo_akmenys <= min(3, akmenu_skaicius):
                break
            print(f"Galite paimti tik nuo 1 iki {min(3, akmenu_skaicius)} akmenų.")
        except ValueError:
            print("Įveskite skaičių nuo 1 iki 3.")

    akmenu_skaicius -= vartotojo_akmenys
    print(f"Jūs paėmėte {vartotojo_akmenys} akmenis. Liko {akmenu_skaicius} akmenų.")

    if akmenu_skaicius == 0:
        print("Jūs paėmėte paskutinį akmenį! Jūs laimėjote!")
        break

    kompiuterio_akmenys = random.randint(1, min(3, akmenu_skaicius))
    akmenu_skaicius -= kompiuterio_akmenys
    print(f"Kompiuteris paėmė {kompiuterio_akmenys} akmenis. Liko {akmenu_skaicius} akmenų.")

    if akmenu_skaicius == 0:
        print("Kompiuteris paėmė paskutinį akmenį! Jūs pralaimėjote!")
        break
