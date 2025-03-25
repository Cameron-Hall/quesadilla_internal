BASIC = 10
REGULAR = 12
SUPERIOR = 16

quesadillas = [["Plain Beef", BASIC, ["beef"]], 
               ["Chicken", BASIC, ["chicken"]],
               ["Vegetarian", BASIC, ["peppers", "beans"]],
               ["Cheesy Beef", REGULAR, ["beef", "cheese"]],
               ["Beef & Beans", REGULAR, ["beef", "beans"]],
               ["Spicy Chicken", REGULAR, ["chicken", "jalapenos", "salsa"]],
               ["Market Fish", REGULAR, ["fish", "capers"]],
               ["The Pablo", SUPERIOR, ["chicken", "bacon", "jalapenos", "cheese", "salsa", "beans"]],
               ["The Bass", SUPERIOR, ["fish", "capers", "chutney", "jalapenos"]],
               ]

def menu(incl_ingredients, no_incl_ingredients, incl_tiers, no_incl_tiers):
    current_menu = quesadillas 
    print("MENU")
    for i in range(len(current_menu)):
        print(f"{current_menu[i][0]:>16} - {current_menu[i][1]} - ", end="")
        for j in range(len(current_menu[i][2])):
            if current_menu[i][2][-1] == current_menu[i][2][j]:
                print(current_menu[i][2][j])
            else:
                print(current_menu[i][2][j], end=", ")
               


def main():
    menu([],[],[],[])

main()