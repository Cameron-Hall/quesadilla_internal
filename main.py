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

extras = [[1, "salsa"],
          [2, "cheese"],
          [3, "beans", "peppers"],
          [4, "capers", "chutney", "jalapenos"],
          [5, "beef", "chicken"],
          [6, "fish"]
          ]


def menu(incl_ingredients, no_incl_ingredients, incl_tiers, no_incl_tiers, incl_extras):
    current_menu = quesadillas 
    print(f"{BOLD + '           Q U E E N S T O W N   Q U E S A D I L L A S' + RESET:^73}")
    print(f"{' '*(WIDTH+2)} |")
    for i in range(0,len(current_menu),2):
        print(f"\033[1m\033[4m{current_menu[i][0]:<{WIDTH}}{current_menu[i][1]}\033[0m | \033[1m\033[4m{current_menu[i+1][0]:<{WIDTH}}{current_menu[i+1][1]}\033[0m")
        print(f"{current_menu[i][3]:<{WIDTH+2}} | {current_menu[i+1][3]:<{WIDTH+2}}\n{' '*(WIDTH+2)} |")

    for i in range(len(extras)):
        print(f"\033[1m\033[4m${extras[i][0]} EXTRAS{' '*(WIDTH-7)}\033[0m") #used special unicode char to work this
        for j in range(len(extras[i])-1):
            if extras[i][-1] == extras[i][j+1]:
                print(f"{extras[i][j+1]}\n")
            else:
                print(extras[i][j+1], end=", ")


def main():
    menu([],[],[],[],bool)


main()