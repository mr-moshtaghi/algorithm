from string import ascii_letters


class CeasarCipher:
    def __init__(self, enc='', dec='', key=0):
        self.enc = enc
        self.dec = dec
        self.letters = ascii_letters
        self.key = key

    def encrypt(self):
        self.letters = ascii_letters
        result = ''

        for ch in self.enc:
            if ch not in ascii_letters:
                result += ch
            else:
                new_key = (ascii_letters.index(ch) + self.key) % len(self.letters)
                result += ascii_letters[new_key]
        return result

    def decrypt(self):
        self.key *= -1
        result = self.encrypt()
        self.key *= -1
        return result


obj = CeasarCipher(enc='ahmad', key=4)
print(obj.encrypt())
