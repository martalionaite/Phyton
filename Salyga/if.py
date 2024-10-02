# Apskaiciuoti skaiciaus kvadrat. Jei Skaicius = 13
# Parasyti laimingas skaicius ir apskaiciuoti jo kvadrata
# sutrumointas salygos sakinys
sk=int(input('Sk = '))
laimingas = sk == 13
kv = sk**2
if laimingas : 
    print('laimingas skaicius')
    print('bet kvadrata jo skaiciuosim')
print(kv)