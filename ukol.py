
soucet = 0
pocet = 0
cisla = []
while True:
    cislo = int(input("Zadejte přirozené číslo (nebo -1 pro konec): "))
    if cislo == -1:
        break
    cisla.append(cislo)
    soucet += cislo
    pocet += 1
if pocet > 0:
    ap = soucet / pocet
    print(f"Aritmetický průměr: {ap}")

    mensi = sum(1 for x in cisla if x < ap)
    vetsi = sum(1 for x in cisla if x > ap)

    print(f"Počet čísel menších než AP: {mensi}")
    print(f"Počet čísel větších než AP: {vetsi}")
else:
    print("Nebyla zadána žádná čísla.")