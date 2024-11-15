# suprogramuoti kuris atlieka veiksmus taip 
# =, -, *, /
# laipsnis ^
# saknies traukimas q
# sk1 + sk2
# sk q

import math 
sk1 = int(input('sk1 = ...'))
veiksmas = input('Pasirinkite operacija +, -, *, /, ^, q   ')
if veiksmas != 'q':
    sk2 = int(input('sk2 = ...'))
match veiksmas:
    case '+':
        ats = sk1 + sk2
    case '-':
        ats = sk1 - sk2
    case '*':
        ats = sk1 * sk2
    case '/':
        ats = sk1 / sk2
    case '^':
        ats = sk1 ** sk2
    case 'q':
        ats = math.sqrt(sk1)
    case _:
        print('Blogai ivesti duomenys')
        viskasOK = False
if viskasOk:
    if veiksmas == 'q':
        print(f'{sk1} {veiksmas} = {ats}')
    else:
        print(f'{sk1} {veiksmas} {sk2} = {ats}')
else : 
    print('pasitikrinkite duomenis')
          
        
        
        
        