import random as r

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

def gen_m(a_prim):
    suma_a_prim = 0
    for element in a_prim:
        suma_a_prim += element
    m = suma_a_prim + r.randint(1, 100)
    return m

def gen_w(m):
    nwd1 = []
    for number in range(int(0.5 * m), m):
        if nwd(number, m) == 1:
            nwd1.append(number)
    w = r.choice(nwd1)
    return w


# Iterative Python 3 program to find
# modular inverse using extended
# Euclid algorithm

# Returns modulo inverse of a with
# respect to m using extended Euclid
# Algorithm Assumption: a and m are
# coprimes, i.e., gcd(a, m) = 1
def inv_mod(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        # q is quotient
        q = a // m
        t = m
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
        # Update x and y
        y = x - q * y
        x = t
        # Make x positive
    if (x < 0):
        x = x + m0
    return x


def gen_klucz_jawny(w, m, a_prim):
    a = []
    for element in a_prim:
        a.append(w * element % m)
    return a

def szyfrowanie(tekst_jawny, a):
    tekst_zaszyfrowany = 0
    for i, bit in enumerate(tekst_jawny):
        tekst_zaszyfrowany += int(bit) * a[i]
    return tekst_zaszyfrowany

def deszyfrowanie(tekst_zaszyfrowany, w_inv_mod, m, a_prim):
    t = tekst_zaszyfrowany * w_inv_mod % m
    tekst_jawny = ""
    for back_element in reversed(a_prim):
        if t >= back_element:
            tekst_jawny += "1"
            t -= back_element
        else:
            tekst_jawny += "0"
    return tekst_jawny[::-1]

def gen_a_prim():
    a_prim = []
    suma = 0
    for i in range(8):
        suma += suma + 110203
        a_prim.append(suma)
    return a_prim

def string_to_bin(tekst):
    binary = ""
    for letter in tekst:
        ascii_code = ord(letter)
        binary += "{0:08b}".format(int(ascii_code))
    return binary

def sentence_to_bin(tekst):
    binary = ""
    for letter in tekst:
        binary += string_to_bin(letter)
    return binary






