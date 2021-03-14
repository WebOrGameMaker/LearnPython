class Menu:
    def __init__(self, elements, position=0):
        self.elements = elements
        self.position = position


    def display(self):
        total = "["
        for i in range(len(self.elements)):
           
            if i == self.position:
                total += "[" + str(self.elements[i]) + "]"
            else:
                total += str(self.elements[i])
            
            if i != len(self.elements) - 1:
                total += ", "

        return total + "]"
    
    def to_the_right(self):
        self.position += 1
        if self.position > len(self.elements) - 1:
            self.position = 0

menu = Menu([1, 2, 3])
print(menu.display())
menu.to_the_right()

print(menu.display())
menu.to_the_right()

print(menu.display())
menu.to_the_right()

print(menu.display())
