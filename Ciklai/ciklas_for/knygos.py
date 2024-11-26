paskutinis_puslapis = 710

skaitmenu_suma = 0

for puslapis in range (1, paskutinis_puslapis + 1):
    skaitmenu_suma += len(str(puslapis))

print(f"Iš viso reikia {skaitmenu_suma} skaitmenų.")