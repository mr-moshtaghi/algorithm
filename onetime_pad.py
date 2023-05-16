import random


def encrypt(text):
    plain = [ord(i) for i in text]
    key = []
    cipher = []

    for p in plain:
        k = random.randint(1, 300)
        c = (p + k) * k
        key.append(k)
        cipher.append(c)

    return cipher, key


def decrypt(cipher, key):
    plain = []
    for i in range(len(cipher)):
        p = int((cipher[i] - key[i] ** 2) / key[i])
        plain.append(chr(p))

    return "".join(plain)


print(encrypt("ahmad"))

print(decrypt([55970, 49280, 68052, 98, 15725], [193, 176, 212, 1, 85]))


