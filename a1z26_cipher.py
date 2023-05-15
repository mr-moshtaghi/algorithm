print(ord('a'))

print(chr(98))


def encode(string):
    return [ord(i) for i in string]


def decode(enc):
    return "".join([chr(i) for i in enc])


print(encode("ahmad"))

print(decode([97, 104, 109, 97, 100]))
