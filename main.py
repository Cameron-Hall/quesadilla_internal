BASIC = 10
REGULAR = 12
SUPERIOR = 16

quesadillas = [["Plain Beef", BASIC, ["beef"]], 
               ["Chicken", BASIC, ["chicken"]],
               ["Vegetarian", BASIC, ["peppers", "beans"]],
               ["Cheesy Beef", REGULAR, ["beef", "cheese"]],
               ["Beef & Beans", REGULAR, ["beef", "beans"]],
               ["Spicy Chicken", REGULAR, ["chicken", "jalapenos", "salsa"]],
               ["Market Fish", REGULAR, ["fish"]],
               ["The Pablo", SUPERIOR, ["chicken", "bacon", "jalapenos", "cheese", "salsa", "beans"]],
               ["The Bass", SUPERIOR, ["fish", "capers", "chutney"]],
               ]

def menu(incl_ingredients, no_incl_ingredients, incl_tiers, no_incl_tiers):
   current_menu = quesadillas 
   print(current_menu)


def main():
    menu([],[],[],[])

main()