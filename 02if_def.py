# Petriukas gavo 3 pazimys
# Apskaiciuoti jo vidurki
# nepamirskim kad 1<=paz<=10
def ivedimas(txt):
    paz = p1 = int(input(f'{txt}=.... '))
    if 1<=paz<=10:
        return paz
    else: 
        print('Blogai ivesti duomenys. Kartokite')
    return ivedimas(txt)

p1 = ivedimas('p1')
p2 = ivedimas('p2')
p3 = ivedimas('p3')
suma =p1 + p2 + p3
vid = suma / 3
print(vid)