import message as m
import keygen as k


def write_to_file(data, line_to_replace):
    my_file = 'dane.txt'
    with open(my_file, 'r') as file:
        lines = file.readlines()
    lines[line_to_replace - 1] = data + '\n'
    with open(my_file, 'w') as file:
        file.writelines(lines)


def read_from_file(read_from_line):
    with open("dane.txt") as dane:
        for i, line in enumerate(dane):
            if i == read_from_line - 1:
                return line[:-1]


def key_creation(line):
    flag5 = True
    value = ''
    while flag5:
        value = input("Please enter the 64-bit key [8 signs] "
                      "or press 'Enter' if You would like to continue with external file key:\n")
        if len(value) == 8:
            write_to_file(value, line)
            flag5 = False
        elif len(value) == 0:
            value = read_from_file(line)
            if len(value) == 8:
                flag5 = False
            else:
                print("The value in external file is not valid")
        else:
            print("Wrong input...")
    return value


cipher = ''
print("This is a program used to encode/decode string data from user input or external .txt file.\n"
      "It uses DES algorithm for both encoding and decoding.\n"
      "Please use only English alphabet for encoding.\n"
      "Choose what You would like to do:\n")
flag1 = True
while flag1:
    print("""
    MENU:
    1. Encoding string message with DES
    2. Decoding binary cipher with DES
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
        print("KEY 1: ")
        key1 = key_creation(8)
        print("KEY 2: ")
        key2 = key_creation(10)
        key1 = k.key_64bit(key1)
        key2 = k.key_64bit(key2)
        if choice == 1:
            key = key_creation(4)
            sub_keys = k.keys_generator(key)
            flag4 = True
            while flag4:
                message = input(
                    "Please write a message to encode or press Enter to continue with external file message...")
                if len(message) == 0:
                    message = read_from_file(2)
                if message.isascii():
                    cipher = m.desx_encode(key, message, key1, key2)
                    print("Your encoded cipher is " + hex(int(cipher, 2)))
                    print("Data has been saved to external file...")
                    flag4 = False
                    write_to_file(hex(int(cipher, 2)), 6)
                    write_to_file(message, 2)
                else:
                    print("Wrong input...")
        elif choice == 2:
            key = key_creation(4)
            sub_keys = k.keys_generator(key)
            flag3 = True
            while flag3:
                cipher = input("Write a binary number to decode the message or press Enter to use external file...")
                if len(cipher) == 0:
                    cipher = read_from_file(6)
                try:
                    int(cipher, 2)
                    if len(cipher) % 64 == 0:
                        flag3 = False
                    else:
                        print("Wrong input...")
                except ValueError:
                    print("Wrong input...")
            message = m.desx_decode(key, cipher, key1, key2)
            write_to_file(cipher, 6)
            write_to_file(message, 2)
            print("Your decoded message is: " + message)
            print("Data has been saved to external file...")
