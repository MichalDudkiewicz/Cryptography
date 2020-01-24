def key_64bit(pub_key):
    enc_key = ''
    for char in pub_key:
        ascii_code = ord(char)
        byte = [0] * 8
        flag = True
        rest = ascii_code
        i = 1
        while flag:
            byte[-i] = rest % 2
            if rest // 2 == 0:
                flag = False
            else:
                rest //= 2
                i += 1
        key_byte = ''.join(map(str, byte))
        enc_key += key_byte
    return enc_key


def key_perm(key, pc):
    perm_key = ''
    for place in pc:
        perm_key += key[place - 1]
    return perm_key


def shift(series, number):
    buffer = series[0:number]
    series = series[number:]
    for bit in buffer:
        series += bit
    return series


def shifts(perm_key):
    left = perm_key[:28]
    right = perm_key[28:]
    shifts_number = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)
    shifted_keys = [''] * 16
    for K in shifted_keys:
        left = shift(left, shifts_number[shifted_keys.index(K)])
        right = shift(right, shifts_number[shifted_keys.index(K)])
        shifted_keys[shifted_keys.index(K)] = left + right
    return shifted_keys


def sub_keys_gen(shifted_keys):
    pc_2 = (14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32)
    sub_keys = [''] * 16
    for shifted_key in shifted_keys:
        sub_keys[shifted_keys.index(shifted_key)] = key_perm(shifted_key, pc_2)
    return sub_keys


def keys_generator(pub_key):
    key = key_64bit(pub_key)
    pc_1 = (57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4)
    perm_key = key_perm(key, pc_1)
    shifted_keys = shifts(perm_key)
    sub_keys = sub_keys_gen(shifted_keys)
    return sub_keys
