class Person:
    def __init__(self, name, like, unlike):
        self.name = name
        self.liked_food = like # a list
        self.unliked_food = unlike # also a list
    def taste(self, food_name):
        if food_name in self.liked_food:
            return f"{self.name.title()} eats {food_name} and loves it! :D" 
        elif food_name in self.unliked_food:
            return f"{self.name.title()} eats {food_name} and hates it! >:("
        return f"{self.name.title()} eats {food_name} and thinks it's okay. :)"

p1 = Person('John', ['ice cream'], ['carrots'])
print(p1.taste('ice cream'))
print(p1.taste('cheese'))
print(p1.taste('carrots'))
