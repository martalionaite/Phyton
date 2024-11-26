import random

while True:
    pasirinkimai = ["žirklės", "popierius", "akmuo"]

    vartotojo_pasirinkimas = input("Įveskite savo pasirinkimą (žirklės, poipierius, akmuo): ").lower()
    if vartotojo_pasirinkimas not in pasirinkimai:
        print("Netinkamas pasirinkimas. Bandykite dar kartą.")
        continue

    kompiuterio_pasirinkimas = random.choice(pasirinkimai)
    print(f"Kompiuterio pasirinkimas: {kompiuterio_pasirinkimas}")

    if vartotojo_pasirinkimas == kompiuterio_pasirinkimas:
        print("Rezultatas: Lygiosios!")
    elif (vartotojo_pasirinkimas == "žirklės" and kompiuterio_pasirinkimas == "popierius") or \
        (vartotojo_pasirinkimas == "popierius" and kompiuterio_pasirinkimas == "akmuo") or \
        (vartotojo_pasirinkimas == "akmuo" and kompiuterio_pasirinkimas == "žirklės"):
        print("Rezultatas: Laimėjote!")
    else:
        print("Rezultatas: Pralaimėjote!")

    dar_karta = input("Ar bandysite dar kart1 (T/N)? ").lower()
    if dar_karta != "t":
        print("Ačiū, kad žaidėte! Iki!")
        break
