# Marks "Show-er ?"

class Student:
    def __init__(self,Science, History):
        self.science = Science
        self.history = History

    def Score(self):
        print("Your marks are in History and Science are:", self.history, self.science)


m1 = Student(54, 87)
m2 = Student(43, 67)

m1.Score()
m2.Score()
