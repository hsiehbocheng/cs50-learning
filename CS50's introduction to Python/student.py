def main():
    student = Student.get()
    # student.house = 'tp' # 因為有 getter 與 setter 避免改寫覆蓋

    print(student)
    # print(f"{student.name} from {student.house}")
    print("Expecto Patronum: ", student.charm())


class Student:
    def __init__(self, name, house, patronus=None):
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self): # print class 時回傳的字串
        return f'{self.name} from {self.house}'
    
    @classmethod # 利用 classmethod，不需要實體化就可以呼叫，例如 Student.get()，並且回傳一個實體化的物件
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return cls(name, house, patronus)
    
    # Getter
    # 定義 getter 與 setter 的好處是可以在設定值時，做一些檢查，例如 name 不可為空值
    @property # 定義 getter，當呼叫 student.name 時，就會執行這個函數
    def name(self):
        return self._name # 加底線是為了讓 init 的 name 與這裡的函數 name 不衝突，但更改 self._name 會影響到 self.name
    
    @name.setter # 定義 setter，當 name 被指定值，例如 student.name = 'Harry'，就會執行這個函數
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

if __name__ == "__main__":
    main()