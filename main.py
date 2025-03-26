BASIC = 10
REGULAR = 12
SUPERIOR = 16

WIDTH = 33

BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

quesadillas = [["Plain Beef", BASIC, ["beef"], "Beef"], 
               ["Chicken", BASIC, ["chicken"], "Chicken"],
               ["Vegetarian", BASIC, ["peppers", "beans"], "Pepper and beans"],
               ["Cheesy Beef", REGULAR, ["beef", "cheese"], "Beef and cheese"],
               ["Beef & Beans", REGULAR, ["beef", "beans"], "Beef and beans"],
               ["Spicy Chicken", REGULAR, ["chicken", "jalapenos", "salsa"], "Chicken, jalapenos and salsa"],
               ["Market Fish", REGULAR, ["fish", "capers"], "Fish and capers"],
               ["The Pablo", SUPERIOR, ["chicken", "beans", "jalapenos", "salsa"], "Chicken, beans, jalapenos and salsa"],
               ["The Bass", SUPERIOR, ["fish", "capers", "jalapenos", "chutney"], "Fish, capers, jalapenos and chutney"],
               ["The Joe", SUPERIOR, ["beef", "peppers", "cheese", "salsa"], "Beef, peppers, cheese and salsa"]
               ]

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
        print(f"\033[1m\033[4m{current_menu[i][0]:<{WIDTH}}{current_menu[i][1]}\033[0m | \033[1m\033[4m{current_menu[i+1][0]:<{WIDTH}}{current_menu[i+1][1]}\033[0m")
        print(f"{current_menu[i][3]:<{WIDTH+2}} | {current_menu[i+1][3]:<{WIDTH+2}}\n{' '*(WIDTH+2)} |")
    print()


def main():
    menu([],[],[],[],bool)


main()