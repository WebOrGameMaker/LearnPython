import time
import sys
from random import randrange
import items

shopping_cart = {} # all your check-out items
spending_amount = 1000
while True:
    userinput = input("What do you want to do?\n\t(1). Search for food\n\t(2). Add food\n\t(3). Exit\nAnswer: ").strip()
    if userinput == "":
        print("Please choose an option.")
    if userinput == "1":
        userinput2 = input("Which category of food do you want to choose——Meat, Vegetal, or Dairy? 'exit' goes to the menu. 'all' gives all the foods. ").lower().strip()
        if userinput2 == "exit":
            break
        elif userinput2 == "":
            print("Please specify a category.")
        elif userinput2 == "easter egg":
            congratulation = "Congrats...🥳🎉🎊🎇You've found the easter egg!🎇🎊🎉🥳\n"
            for letter in congratulation:
                sys.stdout.write(letter)
                sys.stdout.flush()
                seconds = "0." + str(randrange(1, 2, 1))
                seconds = float(seconds)
                time.sleep(seconds)
            time.sleep(1)
            for food4 in items.foods:
                if food4.category == "Easter Egg":
                    chocolate = f"\033[1;33;40m {food4.name}🍫:\n\t💲{food4.price}/{food4.weight_or_quantity} {food4.measured_in}\033[0;37;40m\n"
                    for chocolate_letter in chocolate:
                        sys.stdout.write(chocolate_letter)
                        sys.stdout.flush()
                        seconds = "0." + str(randrange(1, 2, 1))
                        seconds = float(seconds)
                        time.sleep(seconds)
            print("Have a Happy New Year!")
        else:
            found_category = False
            for food in items.foods:
                if food.category.lower().strip() == userinput2 or userinput2 == "all":
                    found_category = True
                    print(food)
            if found_category == False:
                print(f"Category '{userinput2}' does not exist.")
            if found_category:
                while True:
                    userinput3 = input("Do you want to specify the food you want to see? 'exit' returns to the menu. ").lower().strip()
                    if userinput3 == "exit":
                        break
                    elif userinput3 == "":
                        print("Please specify a food.")
                    else:
                        found_food = None
                        for food2 in items.foods:
                            if food2.name.lower().strip() == userinput3:
                                found_food = food2
                                print(f"{food2.name}:\n\tPrice: {food2.price}/{food2.weight_or_quantity} {food2.measured_in}\n\tCategory: {food2.category}")
                        if found_food is not None:
                            while True:
                                userinput4 = input("Do you want to delete or modify this food? 'exit' returns to 'Specific Food' ").lower().strip()
                                if userinput4 == "exit":
                                    break
                                if userinput4 == "delete":
                                    items.foods.remove(found_food)
                                    print(f"You've successfully deleted {found_food}")
                                    break
                                elif userinput4 == "modify":
                                    userinput5 = input("Which part of this food do you want to modify? Enter a number:\n\t(1). Name\n\t(2). Price\n\t(3). Weight/Quantity\nAnswer: ")
                                    if userinput5 == "1":
                                        userinput6 = input("Enter the new name: ")
                                        found_food.name = userinput6
                                        print(f"You've successfully modified {found_food}'s name!")
                                    elif userinput5 == "2":
                                        userinput7 = input("Enter the new price: ")
                                        found_food.price = userinput7
                                        print(f"You've successfully modified {found_food}'s price!")
                                    elif userinput5 == "3":
                                        userinput8 = input("Enter the new weight/quantity: ")
                                        found_food.weight_or_quantity = userinput8
                                        print(f"You've successfully modified {found_food}'s weight/quantity!")
                                    break
                        if found_food is None:
                            print(f"Food/Command '{userinput3}' does not exist.")
    elif userinput == "2":
        while True:
            userinput9 = input("Food Name: ")
            name_found = False
            for food3 in items.foods:
                if userinput9 == food3.name:
                    print(f"Sorry, {userinput9} is already a food.")
                    name_found = True
                    userinput9 = input("Enter another food name: ")
                    break
            if not name_found:
                userinput10 = input("Food Price: ")
                userinput11 = input("Weight/Quantity: ")
                userinput12 = input("Measured In: ")
                userinput13 = input("Food Category: ") 
                new_foond = items.Food(userinput9, userinput10, userinput11, userinput12, userinput13)
                items.foods.append(new_foond)
                print(f"You've added '{userinput9}' to the foods list!")
            break
    elif userinput == "3":
        break
    else:
        print("Please choose a valid option.")
