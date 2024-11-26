kavos_kaina = float(input("Iveskite kavos kaina (eurais, pvz.: 2.20):"))
suma_sukaupta = 0
netinkamos_monetos = 0
tinkamos_monetos = 0

print("Priimamos monetos: 10, 20, 50 centu arba 1, 2 eurai.")

while suma_sukaupta < kavos_kaina:
    moneta = float(input("Imeskite moneta: "))

    if moneta in [0.10, 0.20, 0.50, 1, 2]: 
        suma_sukaupta += moneta
        tinkamos_monetos += 1
        likutis = kavos_kaina - suma_sukaupta
        if likutis > 0:
            print(f"Liko sumokėti: {likutis:.2f} EUR")
        else:
            print(f"Grąža: {abs(likutis):.2f} EUR. Skanios kavos!")
    else:
        print("Netinkama moneta. Meskite dar kartą.")
        netinkamos_monetos += 1

print(f"Tinkamu monetu bandymai: {tinkamos_monetos}")
print(f"Netinkamu monetu bandymai: {netinkamos_monetos}")