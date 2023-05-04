class Allergies:

    def __init__(self, score):
        self.scoret = score

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        ret = []
        list_of_tuples_of_allergies = [
            ("cats",128),
            ("pollen",64),
            ("chocolate",32),
            ("tomatoes",16),
            ("strawberries",8),
            ("shellfish",4),
            ("peanuts",2),
            ("eggs",1)
        ]
        max = 7
        score = self.scoret
        if(self.scoret > 255):
            max += self.scoret//256
            score = self.scoret - 2**max
        for i in list_of_tuples_of_allergies:
            if score >= i[1]:
                ret.append(i[0])
                score -= i[1]
        return ret

print(Allergies(0).allergic_to("peanuts"))