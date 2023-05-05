class School:
    def __init__(self):
        self.added_list = []
        self.grades = {}


    def add_student(self, name, grade):
        for i in self.grades.values():
            for j in i:
                if name == j:
                    self.added_list.append(False)
                    return
        self.grades.setdefault(grade, []).append(name)
        self.added_list.append(True)

    def roster(self):
        t = []
        for i in sorted(self.grades.keys()):
            for j in sorted(self.grades.get(i, [])):
                t.append(j)
        return t

    def grade(self, grade_number):
        return sorted(self.grades.get(grade_number, []))

    def added(self):
        return self.added_list
    
school = School()
school.add_student(name="Peter", grade=2)
school.add_student(name="Anna", grade=1)
school.add_student(name="Barb", grade=1)
school.add_student(name="Zoe", grade=2)
school.add_student(name="Alex", grade=2)
school.add_student(name="Jim", grade=3)
school.add_student(name="Charlie", grade=1)
expected = ["Anna", "Barb", "Charlie", "Alex", "Peter", "Zoe", "Jim"]
print(school.roster())