import re
class Luhn:
    def __init__(self, card_num):
        self.card = card_num.replace(" ", "")

    def valid(self):
        if len(self.card) < 2:
            return False
        x = re.search('\D', self.card)
        if x:
            return False
        rev = self.card[::-1]
        first_val = [int(rev[i])*2 if i % 2 != 0 else int(rev[i]) for i in range(0, len(rev)) ] 
        for i in range(len(first_val)):
            if(first_val[i] > 9):
                first_val[i] -= 9
        if(sum(first_val) % 10 == 0):
            return True
        return False

Luhn("4539 3195 0343 6467").valid()