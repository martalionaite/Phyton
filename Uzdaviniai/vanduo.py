# Vandens saugykloje yra v kubiniu metru vandens (realusis skaicius). Saugyklos vandeni vartoja n zmoniu. Vienas zmogus per para v
# idutiniskai sunaudoja vv kubiniu metru vandens (realus skaicius). Parasykite programa, kuri apskaiciuotu, keliomis paroms p uzteks saugykloje esancio vandens.
# pasitikrinkite kai v = 1001, m = 50, vv=0,1tai p =200.002

v1 = float(input('Vandens saugykloje yra:'))
n1 = int(input('Kiek vartoja saugyklos vandens zmoniu:'))

vv1 = float(input('Zmogus per para sunaudoja vandens:'))

total_vanduo = vv1 / (n1 * v1)


print(f'Vandens saugykloje uztektu {total_vanduo} paromis')