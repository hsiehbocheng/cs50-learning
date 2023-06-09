# def main():
#     name, house = get_student()
#     print(f"Hello, {name} from {house}!")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house

# if __name__ == "__main__":
#     main()

def main():
    student = get_student()
    print(f"{student.name} from {student.house}!")

class Student:
    def __init__(self, name="", house=""):
        self.name = name
        self.house = house

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()