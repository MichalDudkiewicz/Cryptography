import random as r
import key_generator as k


r.seed(a=None, version=2)
a_prim = k.gen_a_prim()
m = k.gen_m(a_prim)
w = k.gen_w(m)
w_inv_mod = k.inv_mod(w, m)
klucz_jawny = k.gen_klucz_jawny(w, m, a_prim)
klucz_prywatny = (w_inv_mod, m, a_prim)
flag1 = True
print(a_prim)
print(m)
print(w)
print(w_inv_mod)
print(klucz_jawny)
print(klucz_prywatny)
while flag1:
    print("""
    MENU:
    1. Encoding string message with knapsack algorithm
    2. Decoding binary cipher with knapsack algorithm
    3. Exit
    """)
    flag2 = True
    choice = ''
    while flag2:
        try:
            choice = int(input())
            if choice in (1, 2, 3):
                flag2 = False
            else:
                print("Wrong input...")
        except ValueError:
            print("Wrong input...")
    if choice == 3:
        flag1 = False
        print("Exiting the program...")
    else:
        if choice == 1:
            tekst_jawny_string = input("Prosze podac tekst jawny: ")
            while len(tekst_jawny_string) % 8 != 0:
                tekst_jawny_string += " "
            tekst_jawny = k.sentence_to_bin(tekst_jawny_string)
            tekst_zaszyfrowany = []
            a = 0
            for byte in range(len(tekst_jawny) // 8):
                tekst_zaszyfrowany.append(k.szyfrowanie(tekst_jawny[a:a + 8], klucz_jawny))
                a += 8
            print("Tekst zaszyfrowany: {}".format(tekst_zaszyfrowany))
        elif choice == 2:
            wybor = input("Czy chcesz rozkodowac wczesniej zakodowana wiadomosc? [y/n]").lower()
            if wybor == "n":
                tekst_zaszyfrowany = []
                ile = input("Ile znakow chcesz zaszyfrowac? ")
                for i in range(int(ile)):
                    znak = int(input("Podaj zaszyfrowany {} znak: ".format(i + 1)))
                    tekst_zaszyfrowany.append(znak)
            tekst_jawny_string2 = ""
            for szyfr in tekst_zaszyfrowany:
                tekst_jawny2 = k.deszyfrowanie(szyfr, w_inv_mod, m, a_prim)
                tekst_jawny_string2 += chr(int(tekst_jawny2, 2))
            print("Tekst jawny: " + tekst_jawny_string2)
