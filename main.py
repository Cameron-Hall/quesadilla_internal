"""Quesadilla ordering system."""
import os
import time

BASIC = [10, "Basic"]
REGULAR = [12, "Regular"]
SUPERIOR = [16, "Superior"]

WIDTH = 33

BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

order = []

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

ingredients = ['beans', 'beef', 'capers', 'cheese', 'chicken', 'chutney', 'fish', 'jalapenos', 'peppers', 'salsa']

extras = [[2, ["cheese", "salsa"], "cheese, salsa"],
          [3, ["beans", "peppers"], "peppers, beans"],
          [4, ["chutney", "jalapenos"], "chutney, jalapenos"],
          [5, ["beef", "chicken"], "beef, chicken"]
          ]


def menu():
    """Print the menu of quesadillas."""
    os.system('cls')
    print(f"{BOLD + '         Q U E E N S T O W N' + RESET:^73}")
    print(f"{BOLD + '         Q U E S A D I L L A S' + RESET:^73}\n")
    print(f"{BOLD + '         M E N U' + RESET:^73}")
    print(f"{' '*(WIDTH+2)} |")
    for i in range(0, len(quesadillas), 2):
        if quesadillas[i] == quesadillas[-1]:
            print(f"\033[1m\033[4m{quesadillas[i][0]:<{WIDTH}}{quesadillas[i][1][0]}\033[0m |")
            print(f"{quesadillas[i][3]:<{WIDTH+2}} |\n{' '*(WIDTH+2)} |")
        else:
            print(f"\033[1m\033[4m{quesadillas[i][0]:<{WIDTH}}{quesadillas[i][1][0]}\033[0m | \033[1m\033[4m{quesadillas[i+1][0]:<{WIDTH}}{quesadillas[i+1][1][0]}\033[0m")
            print(f"{quesadillas[i][3]:<{WIDTH+2}} | {quesadillas[i+1][3]:<{WIDTH+2}}\n{' '*(WIDTH+2)} |")
    input("\nPress enter to continue\n")


def print_item(item):
    """Print a specific item passed into the function, including 'with' and 'without' added items."""
    if item[2][0] == 0:
        without = ""
    else:
        without = f", without {', '.join(item[2][1])}"
    if item[1][0] == 0:
        added = ""
    else:
        added = f", with added {', '.join(item[1][1])}"

    return f"{item[0]}{without}{added}"


def print_order(order):
    """Print the full order."""
    print("Your order currently contains:")
    for i in range(len(order)):
        print(f"{i+1}. {print_item(order[i])}")


def place_order(order):
    """Add items to their current order."""
    while True:
        os.system('cls')
        print("Choose an item from the menu to add to your order. Please use the full name.")
        item_name = input("Alternatively, type 'pass' to not add anything new to your order, or 'menu' to have another look at the menu\n> ").title()
        if item_name == "Pass":
            break
        elif item_name == "Menu":
            menu()
        elif item_name not in quesadilla_names:
            input("That isn't an item on the menu. Press enter to continue")
        else:
            order.append([item_name, [0, []], [0, []]])
            print(item_name, "added to order.")
            time.sleep(1.5)
            break

    return order


def change_order(order):
    """Select items in their order to edit or adjust."""
    while True:
        if not order:
            edited_item = "home"
            break
        os.system('cls')
        print_order(order)
        edited_item = input("Which item from your order would you like to adjust? Enter just the number of the item as listed, or enter 'home' to head back to the home page.\n> ").lower().replace(" ", "")

        if not edited_item.isnumeric() and edited_item != "home":
            input("Invalid entry. Press enter to continue")

        elif edited_item.isnumeric():
            edited_item = int(edited_item)
            if edited_item > len(order):
                input("Invalid entry, this number is higher than the number of items in your order. Press enter to continue")
            elif edited_item == 0:
                input("Invalid entry. Press enter to continue")
            else:
                break

        else:
            break

    while True:
        os.system('cls')
        if edited_item == "home":
            break

        print(f"You are now editing item {edited_item} - {print_item(order[edited_item-1])}")
        try:
            choice = int(input("How would you like to edit your order?\n1. Add ingredients\n2. Remove ingredients\n3. Delete item\n4. Back to homepage\n> "))
        except ValueError:
            print("Invalid entry. Ensure your entry is one of the shown options.")
            time.sleep(1.5)
            continue

        if choice == 1:
            add_ingredient(edited_item, order)
        elif choice == 2:
            remove_ingredient(edited_item, order)
        elif choice == 3:
            order.pop(edited_item-1)
        elif choice == 4:
            pass
        else:
            print("Invalid entry.")
            time.sleep(1.5)
            continue

        break


def add_ingredient(item, order):
    """Add ingredients to individual items on their order."""
    item = item-1
    while True:
        os.system('cls')
        item_ingredients = (list((set(quesadillas[quesadilla_names.index(order[item][0])][2])) ^ set(order[item][2][1]))) + order[item][1][1]
        print(f"What ingredient would you like to add to item {item+1} - {print_item(order[item])}?")
        print(f"It currently contains {', '.join(item_ingredients)}")
        addition = input(f"You can add any of the following, for $3 each:\n{', '.join(ingredients)}\n> ").lower()
        if addition not in ingredients:
            print("That's not an eligible addition.")
            time.sleep(1.5)
            continue
        elif addition in order[item][2][1]:
            order[item][2][1].remove(addition)
            order[item][2][0] -= 1
        else:
            order[item][1][1].append(addition)
            order[item][1][0] += 1
        print(f"{addition.title()} added to item.")
        time.sleep(1.5)
        break


def remove_ingredient(item, order):
    """Remove ingredients from individual items on their order."""
    item = item-1
    while True:
        os.system('cls')
        item_ingredients = (list((set(quesadillas[quesadilla_names.index(order[item][0])][2])) ^ set(order[item][2][1]))) + order[item][1][1]
        print(f"What ingredient would you like to remove from item {item+1} - {print_item(order[item])}?")
        removal = input(f"It contains {', '.join(item_ingredients)}\n> ")
        if removal not in item_ingredients:
            print("That's not an eligible item.")
            time.sleep(1.5)
            continue
        elif removal in order[item][1][1]:
            order[item][1][1].remove(removal)
            order[item][1][0] -= 1
        else:
            order[item][2][1].append(removal)
            order[item][2][0] += 1
        print(f"{removal.title()} removed from item.")
        time.sleep(1.5)
        break


def finalise_order(order):
    """Print final cost and full order."""
    if not order:
        print("Your order is empty!")
        time.sleep(1.5)
        return False
    else:
        print_order(order)
        total_cost = 0
        for item in order:
            total_cost += quesadillas[quesadilla_names.index(item[0])][1][0]
            total_cost += 3 * item[1][0]
        print(f"Your order total comes to ${total_cost}")
        return True


def main(order):
    """Choose what to do with ordering system"""
    os.system("cls")
    while True:
        os.system("cls")
        choice = input("1. View menu\n2. Add items to order\n3. Edit parts of your order\n4. Show order\n5. Finalise your order\n> ")
        os.system("cls")
        if choice == "1":
            menu()

        elif choice == "2":
            order = place_order(order)

        elif choice == "3":
            change_order(order)

        elif choice == "4":
            if not order:
                print("Your order is empty!")
                time.sleep(1.5)
            else:
                print_order(order)
                print("Press enter to continue")
            

        elif choice == "5":
            if finalise_order(order):
                break            

        else:
            print("Invalid entry.")
            time.sleep(2)


main(order)
