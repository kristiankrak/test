odd_numbers = [num for num in range(1, 21) if num % 2 != 0] #num nastaví se na aktuální číslo.Když num % 2 vrátí 0, znamená to, že je číslo sudé (dělí se 2 bez zbytku). Pokud vrátí něco jiného (v tomto případě 1), číslo je liché.
print(odd_numbers)
