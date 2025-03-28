BASIC = [10,"Basic"]
REGULAR = [12,"Regular"]
SUPERIOR = [16, "Superior"]

WIDTH = 33

BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

quesadillas = [["Plain Beef", BASIC, ["beef"], "beef"], 
               ["Chicken", BASIC, ["chicken"], "chicken"],
               ["Vegetarian", BASIC, ["peppers", "beans"], "pepper and beans"],
               ["Cheesy Beef", REGULAR, ["beef", "cheese"], "beef and cheese"],
               ["Beef & Beans", REGULAR, ["beef", "beans"], "beef and beans"],
               ["Spicy Chicken", REGULAR, ["chicken", "jalapenos", "salsa"], "chicken, jalapenos and salsa"],
               ["Market Fish", REGULAR, ["fish", "capers"], "fish and capers"],
               ["The Pablo", SUPERIOR, ["chicken", "beans", "jalapenos", "salsa"], "chicken, beans, jalapenos and salsa"],
               ["The Bass", SUPERIOR, ["fish", "capers", "jalapenos", "chutney"], "fish, capers, jalapenos and chutney"],
               ["The Joe", SUPERIOR, ["beef", "peppers", "cheese", "salsa"], "beef, peppers, cheese and salsa"]
               ]

quesadilla_names = ['Plain Beef', 'Chicken', 'Vegetarian', 'Cheesy Beef', 'Beef & Beans', 'Spicy Chicken', 'Market Fish', 'The Pablo', 'The Bass', 'The Joe']

extras = [[2, ["cheese", "salsa"], "cheese, salsa"],
          [3, ["beans", "peppers"], "peppers, beans"],
          [4, ["chutney", "jalapenos"], "chutney, jalapenos"],
          [5, ["beef", "chicken"], "beef, chicken"]
          ]


def menu(incl_ingredients, no_incl_ingredients, incl_tiers, no_incl_tiers, incl_extras):
    current_menu = quesadillas 
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


def place_order(order):
    while True:
        print("Choose an item from the menu to add to your order. Please use the full name.", end=" ")
        item = input("Alternatively, type 'pass' to not add anything new to your order\n> ").title()
        if item not in quesadilla_names:
            print("That isn't an item on the menu")
        else:
            order.append([item,[],[]])
            return order


def change_order(order):
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
    choice = input("Which item from your order would you like to adjust? Enter just the number of the item as listed.")

    

    print("How would you like to adjust your order?")
    choice = input("> ")
    if choice == "1":
        remove_ingredient()


def remove_ingredient(item):
    if quesadillas[quesadilla_names.index(item)][1] in [BASIC, SUPERIOR]:
        print(f"You are not allowed to remove items from {quesadillas[quesadilla_names.index(item)][1][1]} quesadillas.")
    else:
        print(f"Would you like to remove anything from this quesadilla? This quesadilla contains {quesadillas[quesadilla_names.index(item)][-1]}\nList any items you'd like to remove one at a time, or type 'none' if you'd like to keep the quesadilla as is.")
        removal_list = []
        while True:
            if quesadillas[quesadilla_names.index(item)][1] in [BASIC, SUPERIOR]:
                break
            removal = input(">  ").lower()
            if removal not in quesadillas[quesadilla_names.index(item)][-2] and removal != "none":
                print(f"That's not an item in the {item} quesadilla. The items in this quesadilla are {quesadillas[quesadilla_names.index(item)][-1]}")
            else:
                if removal == "none":
                    break
                else:
                    removal_list.append(removal)
                    if quesadillas[quesadilla_names.index(item)][1] == REGULAR:
                        break
            print(f"Choose an item (out of {', '.join(set(quesadillas[quesadilla_names.index(item)][-2])^set(removal_list))}) to remove, type 'none' to keep the quesadilla as is or type 'reset' to reset the quesadilla to its original ingredients.")

        print(quesadillas[quesadilla_names.index(item)][-1])
        print(removal_list)


def finalise_order():
    print("Order complete")


def main():
    order = []
    while True:
        choice = input("> ")
        if choice == "1":
            menu([],[],[],[],bool)
        elif choice == "2":
            place_order(order)
        elif choice == "3":
            change_order(order)
        elif choice == "4":
            finalise_order(order)

main()