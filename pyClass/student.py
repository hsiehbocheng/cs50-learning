def main():
    student = get_student()
    # student.house = 'tp' # 因為有 getter 與 setter 避免改寫覆蓋
    print(student)
    # print(f"{student.name} from {student.house}")
    print("Expecto Patronum: ", student.charm())

class Student:
    def __init__(self, name, house, patronus):
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self): # print class 時回傳的字串
        return f'{self.name} from {self.house}'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name is required.")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ['Taipei', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
            raise ValueError("Invalid house")
        self._house = house
    
    def charm(self):
        if self.patronus == 'otter':
            return "🐼"
        elif self.patronus == 'Dog':
            return "🐶"
        else:
            return "😀"

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()