x = int(input("Podaj liczbe od 1 do 100"))
if x < 1 or x > 100:
    print("Liczba musi być z przedzialu 1 do 100 !")
elif x == 1:
    print(x)
else:
    while x != 1:
        print(x)
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1

