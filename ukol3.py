def je_prvocislo(cislo):
    if cislo < 2:
        return False
    for i in range(2, int(cislo**0.5) + 1):
        if cislo % i == 0:
            return False
    return True

prvocisla = [cislo for cislo in range(1, 21) if je_prvocislo(cislo)]
print(prvocisla)