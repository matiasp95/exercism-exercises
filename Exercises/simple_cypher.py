import secrets

LETTERS = "abcdefghijklmnopqrstuvwxyz"
class Cipher:
    def __init__(self, key=None):
        self.key = key or "".join(secrets.choice(LETTERS) for i in range(100))

    def encode(self, text):
        if len(self.key)<len(text):
            self.key = self.key*len(text)
        res = [LETTERS[(LETTERS.find(self.key[i])+LETTERS.find(text[i]))%len(LETTERS)] for i in range(len(text))]
        return ''.join(res)

    def decode(self, text):
        if len(self.key)<len(text):
            self.key = self.key*len(text)
        res = [LETTERS[(LETTERS.find(text[i])-LETTERS.find(self.key[i]))%len(LETTERS)] for i in range(len(text))]
        return ''.join(res)

print(Cipher("aaaaaaaaaaaaaaaaaa").encode("iamapandabear"))
print(Cipher("dddddddddddddddddddd").decode("ldpdsdqgdehdu"))