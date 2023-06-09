import random   

    
class Hat:

    houses = ['Gry', 'Huff', 'Raven', "Sly"]

    @classmethod # 當這個 class 只會有一個，不會有多次實體化的時候，就可以用 classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(f"{name} from {house}")


Hat.sort("Harry")