# ivedimas skaicius. Jei jis lyginis apskaiciuoti jo kvadrata
# jei nelyginis - pakelti kubu
def kvadratas(sk):
    rez = sk ** 2
    return rez

def kubas(sk):
    rez = sk ** 3
    return rez

sk = int(input('sk = ...'))
if sk % 2 == 0:
    rez = kvadratas(sk)
else:
    rez = kubas(sk)
print(rez)