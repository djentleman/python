import random, time, math

class People:
    def __init__ (self):
            self.gender = self.gender(random.randint(0,66))
            self.money = random.randint(1000, 1000000)
            self.intellgents = random.randint(1, 100)
            self.soical = random.randint(1, 100)
            self.love = random.randint(1, 100)
            self.mean = random.randint(1, 100)
            self.currentThought = ""
            self.name = "bob"
            self.x = random.randint(1, 500)
            self.y = random.randint(1, 500)
            self.color = self.colour(self.money)
            self.width = 3

#randommly genarates a gender 
    def gender(self, seed):
        if seed == 0:
            return "Male"
        else:
            print("win")
            return "Female"

        
#depending on how much money you have changes your colour
    def colour(self, money):
        if money < 1000:
            return "red"
        elif money < 10000:
            return "yellow"
        elif money < 100000:
            return "blue"
        else:
            return "green"
        
gender(100)
