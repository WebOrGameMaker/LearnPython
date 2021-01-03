class Food:
    def __init__(self, name, price, weight_or_quantity, measured_in, category):
        self.name = name
        self.price = price
        self.weight_or_quantity = weight_or_quantity
        self.measured_in = measured_in
        self.category = category

    def __str__(self): # only used once :(
        return f"{self.name}. Price: {self.price}/{self.weight_or_quantity} {self.measured_in}. "


foods = [
    # Meat Section
    Food("Organic Beef", 8.99, 1, "pound", "Meat"),
    Food("Organic Pork", 3.49, 1, "pound", "Meat"),
    Food("Organic Lamb/Mutton", 9.99, 1, "pound", "Meat"),
    Food("Organic Chicken", 3.99, 1, "pound", "Meat"),
    Food("Organic Turkey", 2.99, 1, "pound", "Meat"),
    Food("Organic Venison", 8.99, 1, "pound", "Meat"),
    Food("Organic Peking Duck", 5.99, 1, "pound", "Meat"),
    Food("Organic Wild Boar", 12.99, 1, "pound", "Meat"),
    Food("Organic Bison", 15.99, 1, "pound", "Meat"),
    Food("Organic Goose", 9.99, 1, "pound", "Meat"),
    Food("Organic Rabbit", 1.49, 1, "pound", "Meat"),
    Food("Organic Pheasant", 4.99, 1, "pound", "Meat"),
    # Vegetal Section
    Food("Organic Green Cabbage Head", 2.49, 1, "item", "Vegetal"),
    Food("Organic Lettuce", 1.49, 1, "pound", "Vegetal"),
    Food("Organic Baby Spinach", 1.99, 5, "oz", "Vegetal"),
    Food("Organic Carrots", 0.99, 1, "pound", "Vegetal"),
    Food("Organic Tomato", 2.99, 1, "pound", "Vegetal"),
    Food("Organic Potato", 1.29, 1, "pound", "Vegetal"),
    # Dairy Section
    Food("Organic Milk", 4.99, 1, "item", "Dairy"),
    Food("Organic Cheese", 2.99, 1, "pound", "Dairy"),
    Food("Neapolitan Ice Cream", 15.99, 1, "pound", "Dairy"),
    # Nothing to see here😉...
    Food("Awesome Microsoft Python-Looking Quantum Computer", 9_999_999_999_999_999, 1, "item", "Easter Egg") # 
    ]
