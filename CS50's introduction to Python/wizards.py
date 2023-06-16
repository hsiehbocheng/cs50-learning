class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Name is required.")
        self.name = name

class Student(Wizaed):
    def __init__(self, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
wizard = Wizard("Harry")    
student = Student("Harry", "Gryffindor")
professor = Professor("Snape", "Potions")