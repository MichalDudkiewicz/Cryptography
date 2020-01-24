import keygen as keygen


def split_message(message, n):
    if len(message) % n != 0:
        message += ' ' * (n - len(message) % n)
    blocks_amount = len(message) // n
    message_blocks = [''] * blocks_amount
    i = 0
    n_block = 0
    for letter in message:
        i += 1
        message_blocks[n_block] += letter
        if i % n == 0:
            i = 0
            n_block += 1
    return message_blocks


def binary_message_blocks(message_blocks):
    blocks_amount = len(message_blocks)
    bin_blocks = [''] * blocks_amount
    for i, block in enumerate(bin_blocks):
        bin_blocks[i] += keygen.key_64bit(message_blocks[i])
    return bin_blocks


def xor(series1, series2):
    result = ''
    for i, bit in enumerate(series1):
        if bit == '0' and series2[i] == '0':
            result += '0'
        elif bit == '1' and series2[i] == '1':
            result += '0'
        else:
            result += '1'
    return result


def perm_s(xor_blocks):
    result = ''
    s1 = ((14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7),
          (0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8),
          (4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0),
          (15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13))
    s2 = ((15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10),
          (3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5),
          (0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15),
          (13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9))
    s3 = ((10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8),
          (13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1),
          (13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7),
          (1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12))
    s4 = ((7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15),
          (13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9),
          (10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4),
          (3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14))
    s5 = ((2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9),
          (14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6),
          (4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14),
          (11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3))
    s6 = ((12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11),
          (10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8),
          (9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6),
          (4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13))
    s7 = ((4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1),
          (13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6),
          (1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2),
          (6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12))
    s8 = ((13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7),
          (1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2),
          (7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8),
          (2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11))
    s = (s1, s2, s3, s4, s5, s6, s7, s8)
    for i in range(8):
        tab_s = s[i]
        row = int(xor_blocks[i][0] + xor_blocks[i][-1], 2)
        column = int(xor_blocks[i][1:-1], 2)
        result += "{0:04b}".format(tab_s[row][column])
    return result


IP = (58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7)


def des(key, word, if_decoding=False):
    p = (16, 7, 20, 21,
         29, 12, 28, 17,
         1, 15, 23, 26,
         5, 18, 31, 10,
         2, 8, 24, 14,
         32, 27, 3, 9,
         19, 13, 30, 6,
         22, 11, 4, 25)
    ip2 = (40, 8, 48, 16, 56, 24, 64, 32,
           39, 7, 47, 15, 55, 23, 63, 31,
           38, 6, 46, 14, 54, 22, 62, 30,
           37, 5, 45, 13, 53, 21, 61, 29,
           36, 4, 44, 12, 52, 20, 60, 28,
           35, 3, 43, 11, 51, 19, 59, 27,
           34, 2, 42, 10, 50, 18, 58, 26,
           33, 1, 41, 9, 49, 17, 57, 25)
    e_bit = (32, 1, 2, 3, 4, 5,
             4, 5, 6, 7, 8, 9,
             8, 9, 10, 11, 12, 13,
             12, 13, 14, 15, 16, 17,
             16, 17, 18, 19, 20, 21,
             20, 21, 22, 23, 24, 25,
             24, 25, 26, 27, 28, 29,
             28, 29, 30, 31, 32, 1)
    cipher = ''
    left = word[:32]
    right = word[32:]
    sub_keys = []
    if if_decoding is False:
        sub_keys = keygen.keys_generator(key)
    else:
        for i in reversed(keygen.keys_generator(key)):
            sub_keys.append(i)
    for sub_key in sub_keys:
        perm_right = keygen.key_perm(right, e_bit)
        xor_right = xor(perm_right, sub_key)
        xor_blocks = split_message(xor_right, 6)
        perm_s_right = perm_s(xor_blocks)
        perm2_right = keygen.key_perm(perm_s_right, p)
        buf = right
        right = xor(perm2_right, left)
        left = buf
    buf = right
    right = left
    left = buf
    new = left + right
    cipher += keygen.key_perm(new, ip2)
    return cipher


# def des_encode(key, message):
#     message_blocks = split_message(message, 8)
#     bin_blocks = binary_message_blocks(message_blocks)
#     binary_cipher_blocks = []
#     for i, block in enumerate(bin_blocks):
#         perm_bin_block = keygen.key_perm(bin_blocks[i], IP)
#         binary_cipher = des(key, perm_bin_block)
#         binary_cipher_blocks.append(binary_cipher)
#     result = ''.join(binary_cipher_blocks)
#     return result


def desx_encode(key, message, key1, key2):
    message_blocks = split_message(message, 8)
    bin_blocks = binary_message_blocks(message_blocks)
    binary_cipher_blocks = []
    for i, block in enumerate(bin_blocks):
        xored_bin_block = xor(bin_blocks[i], key1)
        perm_bin_block = keygen.key_perm(xored_bin_block, IP)
        binary_cipher = des(key, perm_bin_block)
        xored_bin_block = xor(binary_cipher, key2)
        binary_cipher_blocks.append(xored_bin_block)
    binary_cipher = ''.join(binary_cipher_blocks)
    return binary_cipher


# def des_decode(key, binary_cipher):
#     output = ''
#     binary_cipher_blocks = split_message(binary_cipher, 64)
#     for block in binary_cipher_blocks:
#         perm_cipher = keygen.key_perm(block, IP)
#         message_back = des(key, perm_cipher, True)
#         message_back = split_message(message_back, 8)
#         for byte in message_back:
#             output += (chr(int(byte, 2)))
#     return output


def desx_decode(key, binary_cipher, key1, key2):
    output = ''
    binary_cipher_blocks = split_message(binary_cipher, 64)
    for block in binary_cipher_blocks:
        block = xor(block, key2)
        perm_cipher = keygen.key_perm(block, IP)
        message_back = des(key, perm_cipher, True)
        message_back = xor(message_back, key1)
        message_back = split_message(message_back, 8)
        for byte in message_back:
            output += (chr(int(byte, 2)))
    return output
