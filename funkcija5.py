# Kad programa veiktu reikia 3 rezultatu
# 1. Duomenu ivedimas
# 2. Veiksmus
# 3. Rezultata

# sudeti 2 skaicius
# su 3 funkcijom

def ivedimas(txt):
    sk = int(input(f'{txt} = ...'))
    return sk

def veiksmai():
   a = ivedimas('sk1')
   b = ivedimas('sk2')
   rez = a + b
   return a, b, rez

def rezultatas():
    skaicius1, skaicius2, ats = veiksmai()
    print(f'{skaicius1} + {skaicius2} = {ats}')

rezultatas()