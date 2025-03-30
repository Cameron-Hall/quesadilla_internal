import os

BASIC = [10,"Basic"]
REGULAR = [12,"Regular"]
SUPERIOR = [16, "Superior"]

WIDTH = 33

BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

quesadillas = [("Plain Beef", BASIC, ("beef"), "beef"),
               ("Chicken", BASIC, ("chicken"), "chicken"),
               ("Vegetarian", BASIC, ("peppers", "beans"), "pepper and beans"),
               ("Cheesy Beef", REGULAR, ("beef", "cheese"), "beef and cheese"),
               ("Beef & Beans", REGULAR, ("beef", "beans"), "beef and beans"),
               ("Spicy Chicken", REGULAR, ("chicken", "jalapenos", "salsa"), "chicken, jalapenos and salsa"),
               ("Market Fish", REGULAR, ("fish", "capers"), "fish and capers"),
               ("The Pablo", SUPERIOR, ("chicken", "beans", "jalapenos", "salsa"), "chicken, beans, jalapenos and salsa"),
               ("The Bass", SUPERIOR, ("fish", "capers", "jalapenos", "chutney"), "fish, capers, jalapenos and chutney"),
               ("The Joe", SUPERIOR, ("beef", "peppers", "cheese", "salsa"), "beef, peppers, cheese and salsa")
               ]

quesadilla_names = ['Plain Beef', 'Chicken', 'Vegetarian', 'Cheesy Beef', 'Beef & Beans', 'Spicy Chicken', 'Market Fish', 'The Pablo', 'The Bass', 'The Joe']

extras = [[2, ["cheese", "salsa"], "cheese, salsa"],
          [3, ["beans", "peppers"], "peppers, beans"],
          [4, ["chutney", "jalapenos"], "chutney, jalapenos"],
          [5, ["beef", "chicken"], "beef, chicken"]
          ]

filters = [0, [], ["",True]]
filtered = []

def menu(filter_bool):
    current_menu = [item for item in quesadillas if item not in filtered]
    print(f"{BOLD + '         Q U E E N S T O W N' + RESET:^73}")
    print(f"{BOLD + '         Q U E S A D I L L A S' + RESET:^73}\n")
    print(f"{BOLD + '         M E N U' + RESET:^73}")
    print(f"{' '*(WIDTH+2)} |")
    for i in range(0,len(current_menu),2):
        if current_menu[i] == current_menu[-1]:
            print(f"\033[1m\033[4m{current_menu[i][0]:<{WIDTH}}{current_menu[i][1][0]}\033[0m |")
            print(f"{current_menu[i][3]:<{WIDTH+2}} |\n{' '*(WIDTH+2)} |")
        else:
            print(f"\033[1m\033[4m{current_menu[i][0]:<{WIDTH}}{current_menu[i][1][0]}\033[0m | \033[1m\033[4m{current_menu[i+1][0]:<{WIDTH}}{current_menu[i+1][1][0]}\033[0m")
            print(f"{current_menu[i][3]:<{WIDTH+2}} | {current_menu[i+1][3]:<{WIDTH+2}}\n{' '*(WIDTH+2)} |")
    print()

    if filter_bool and filtered:
        print(f"Your current filters are:\nPrice: {filters[0]}\nIngredients: {filters[1].join(", ")}\n\nType R to remove all filters or Y to add another filter")

    elif filter_bool:
        choice = input("Would you like to view the menu with any filters (Y/N) ?\n> ").upper()

    else:
        input("Press enter to continue")

    while True:
        if not filter_bool:
            break

        if choice not in ["Y", "YES", "N", "NO", "R"]:
            print("Invalid entry, please enter Y or N to indicate yes or no.")

        else:
            if choice in ["Y", "YES"]:
                while True:
                    choice = input("What would you like to filter by?\n1. Price\n2. Ingredients\n3. Back to menu\n> ")

                    if choice not in ["1", "2", "3"]:
                        print("Invalid entry.")

                    elif choice == "1":

                        while True:
                            price_range = input("What price range would you like to filter with? Separate your minimum and maximum value with a hyphen, like this: 10-14\n> ")
                            price_range = price_range.replace(" ","")
                            try:
                                hyphen_loc = price_range.index('-')
                            except ValueError:
                                print("Invalid entry. Please ensure your minimum and maximum price values are separated by a hyphen.")
                                continue
                            try:
                                minimum = int(price_range[:hyphen_loc])
                                if 0 > minimum or minimum > 100:
                                    raise ValueError
                                else:
                                    maximum = int(price_range[hyphen_loc+1:])
                                    if 0 > maximum or maximum > 100:
                                        raise ValueError
                                    else:
                                        break
                            except ValueError:
                                print("Invalid entry. Please ensure you use whole numbers greater than 0 and less than 100.")
                        for quesadilla in quesadillas:
                            if maximum >= quesadilla[1][0] and minimum <= quesadilla[1][0]:
                                pass
                            else:
                                filtered.append(quesadilla)
                                filters[0] = "10-14"
                        
                        menu(True)

            elif choice == "R":
                filters = [0, [], ["",True]]
                filtered = []

            else:
                os.system('clear')
                menu(False) 


def place_order(order):
    
    while True:
        print("Choose an item from the menu to add to your order. Please use the full name.", end=" ")
        item = input("Alternatively, type 'pass' to not add anything new to your order, or 'menu' to have another look at the menu\n> ").title()
        if item == "Pass":
            pass
        elif item == "Menu":
            menu()
        elif item not in quesadilla_names:
            print("That isn't an item on the menu")
        else:
            order.append([item,[0,[]],[0,[]]])
            return order


def change_order(order):

    if not order:
        print("You can't edit parts of your order, it's empty!")
        pass

    while True:
        print("Your order currently contains:")
        loop_num = 1

        for item in order:
            if item[1] or item[2]:
                print(f"{loop_num}. {item[0]}", end = " - ")
            else:
                print(f"{loop_num}. {item[0]}")

            if item[1]:
                print("without ")

                for removal in item[1]:
                    if removal == item[1][-1] and item[2]:
                        print(removal, end= ", ")
                    elif not item[2]:
                        print(removal)
                    else:
                        print(removal, end= " and ")

            if item[2]:
                print("with ")

                for addition in item[2]:
                    if addition == item[2][-1]:
                        print(addition, end= ", ")
                    else:
                        print(addition)

            loop_num += 1

        try:
            adjusted_item = int(input("Which item from your order would you like to adjust? Enter just the number of the item as listed, or enter '0' to head back to the main menu.\n> "))

            if adjusted_item > len(order):
                raise ValueError
            
        except ValueError:
            print(f"Invalid entry. Please enter a number between 0 and {len(order)}")

        print("hi")
        if adjusted_item == 0:
            pass

        else:
            print(f"You are now editing item {adjusted_item}")
            choice = input("1. Add ingredients\n2. Remove ingredients\n3. Remove item\n> ")
            if choice == "1":
                add_ingredient()
            elif choice == "2":
                remove_ingredient()
            elif choice == "3":
                print(f"Item {adjusted_item}")
                order.pop(adjusted_item-1)


def add_ingredient(item):
    pass


def remove_ingredient(item):
    pass


def finalise_order(order):
    if not order:
        print("Your order is empty!")
        pass
    else:
        print("Order complete")


def main():
    order = []
    while True:
        choice = input("1. View menu\n2. Add items to order\n3. Edit parts of your order\n4. Finalise your order\n> ")

        if choice == "1":
            menu(True)

        elif choice == "2":
            order = place_order(order)

        elif choice == "3":
            change_order(order)

        elif choice == "4":
            finalise_order(order)

        else:
            print("Invalid entry.")

main()
