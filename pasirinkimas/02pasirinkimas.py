# Ivedama savaites diena skaiciumi tarkim 1 parasyti pirmadienis 
diena = int(input('darbo diena ar savaitgalis...'))
match diena:
    case 1|2|3|4|5:
        txt = 'Darbo diena'
    case 6|7:
        txt = 'savaitgalis'
    case _:
        txt = 'Blogai ivesti duomenys'

print(f'{diena} ----> {txt}')