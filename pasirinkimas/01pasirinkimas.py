# Ivedama savaites diena skaiciumi tarkim 1 parasyti pirmadienis 
diena = input('Iveskite savaites diena skaiciumi...')
match diena:
    case '1':
        txt = 'pirmadienis'
    case '2':
        txt = 'antradienis'
    case '3':
        txt = 'treciadienis'
    case '4':
        txt = 'ketvirtadienis'
    case '5':
        txt = 'penktadienis'
    case '6':
        txt = 'sestadienis'
    case '7':
        txt = 'sekmadienis'
    case _:
        txt = 'Blogai ivesti duomenys'

print(f'{diena} ----> {txt}')