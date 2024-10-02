# Mokinio pazymiai
# -begalybes iki ----> negalimas pazimys
# 1 iki 3 -----> blogas pazimys
# 4 iki 6 ---> patenkinamas
# 7 iki 9 ----> geras
# 10 -----> puikus
# nuo 11 iki + begalybes negalimas pazimys

paz = int(input('Koks pazimys?'))
if paz >= 1 and paz <= 3:
    print('Blogas pazimys')
elif paz >= 4 and paz <= 6:
    print('Patenkinimas')
elif paz >= 7 and paz <= 9:
    print('Geras pazimys')
elif paz ==10:
    print('Puiku')
else:
    print('Negalimas pazimys')
