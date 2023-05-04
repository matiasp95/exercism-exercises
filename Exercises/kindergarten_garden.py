plants_dict = {
    "V": "Violets",
    "R": "Radishes",
    "C": "Clover",
    "G": "Grass"
}
class Garden:
    def __init__(self, diagram, students = ["Alice", "Bob", "Charlie", "David",
                        "Eve", "Fred", "Ginny", "Harriet",
                        "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.students = sorted(students)
        self.garden = diagram.split("\n")
    def plants(self, student):
        pos = self.students.index(student)
        plants_rows = [i[pos*2:pos*2+2] for i in self.garden]
        return [plants_dict[letter] for row in plants_rows for letter in row]
    
print(Garden("VVCG\nVVRC").plants("Bob"))