# Dictionaries
# The list of items in grocery store including categories
dictItems = {"Dairy":[["Milk",2.30], ["Butter",4.50], ["Eggs",3.40], ["Cheese slices",3.15],
                    ["Evaporated Milk Creamer",1.40], ["Milo",12.50], ["Biscuits",5.30], ["Yogurt",0.95]],

            "Packaged Goods":[["Bread",2.70], ["Cereal",7.00], ["Crackers",3.10], ["Chips",2.60], ["Raisin",2.10],
                            ["Nuts",2.00], ["Green Bean",1.05], ["Barley",1.05]],

            "Canned Goods": [["Tomato",1.45], ["Button Mushroom",1.15], ["Baking Bean",1.35], ["Tuna Fish",1.45],
                        ["Kernel Corn",1.25], ["Sardine Fish",1.10], ["Chicken Luncheon Meat",1.95],
                        ["Pickled Lettuce", 0.95]],

            "Condiments/Sauces": [["Fine Salt", 0.80], ["Sea Salt Flakes", 1.30], ["Chicken Stock", 3.15],
                                  ["Chilli Sauce", 2.65], ["Oyster Sauce", 4.50], ["Sweet Soy Sauce", 3.75],
                                  ["Tomato Ketchup", 3.20], ["Sesame Oil", 4.95]],

            "Drinks & Beverages": [["Green Tea Canned 330 ML",15.00], ["Blackcurrant Ribena 330 ML",31.00],
                                   ["100 Plus 24 Cans",15.00], ["Orange Cordial 2 Litre",3.90],
                        ["Mineral Water 24 x 600 ML",7.00], ["Pineapple juice",0.80], ["Nescafe Coffee",9.90],
                        ["Coke 24 Cans", 12.40]]}


#----------------------------------------------------------------------------------------------------------------------#
# Lists
listID = []  # an empty array to contain all the items id in cart
categoryList = []  # an empty array to contain all the items category in cart
cartList = []  # an empty array to contain all the items in cart
unitpriceList = []  # an empty array to contain the unit price of the items in cart
quantityList = []  # an empty array contain all the quantity of items in cart
subList = []  # an empty array to contain the subtotal of the items in cart

#----------------------------------------------------------------------------------------------------------------------#
# About Triple Ins Grocery
print("------------------------------------------------------------------------")
print("{:^65s}".format("Welcome to TRIPLE INS' GROCERY 0.0"))
print("------------------------------------------------------------------------")
print("We are a small company of 2, selling highly-rich and fresh groceries.")
print("There are many various items in each categories for you to choose from.")
print("Enjoy shopping!")
print("")

#----------------------------------------------------------------------------------------------------------------------#
# Main Program
def main():
    while True:
        print("")
        print("-------------------------------")
        print("{:^30s}".format("Main Menu"))
        print("-------------------------------")
        print("1. Sign Up/Login")
        print("2. View Menu")
        print("3. Place Orders")
        print("4. View Orders Placed")
        print("5. Remove Existing Orders")
        print("6. Payment/CheckOut")

        print("")
        myOption = int(input('Please enter your option (1-6): '))  # ask user to enter their option of their choice
        print("")

        if myOption == 1:  # if user option is 1
            log_page()  # go to signup/login page

        if myOption == 2:  # if user option is 2
            show_items()  # go to view menu page

        elif myOption == 3:  # if user option is 3
            add_items()  # go to place orders

        elif myOption == 4:  # if user option is 4
            view_items()  # go to view orders page

        elif myOption == 5:  # if user option is 5
            remove_items()  # go to remove orders page

        elif myOption == 6:  # if user option is 6
            payment_checkout()  # go to payment/checkout page

        else:
            print("")

#----------------------------------------------------------------------------------------------------------------------#
# SignUp/Login Menu
def log_page():
    while True:
        print("-------------------------------")
        print("{:^30s}".format("Login/SignUp"))
        print("-------------------------------")
        print("1. Sign Up For An Account")
        print("2. Login Your Account")
        print("")

        myOption = int(input('Please enter your option (1-2): '))  # ask user to enter their option of their choice
        print("")

        if myOption == 1:  # if user option is 1
            signUp()  # go to sign up page

        elif myOption == 2:  # if user option is 2
            login()  # go to login page

        else:
            print("")

#----------------------------------------------------------------------------------------------------------------------#
# Sign Up Page
def signUp():
    sign = input("Do you want to sign up for an account? [yes/no]: ")  # ask user if they want to sign up for an account
    print("")

    if sign == "yes":  # if user want to sign up for an account
        print("-----------------------------------")
        print("{:^35s}".format("Sign Up For An Account"))
        print("-----------------------------------")

        global sign_user  # declare a global sign_user variable to be used later when applicable
        global address_user  # declare a global address_user variable to be used later in payment page

        sign_user = input("Please enter Username: ")  # user to enter their username to sign up
        address_user = input("Please enter Home Address: ")  # user to enter their home address
        print("")
        print("Signed up successfully.")
        print("")

        # print the user personal details
        print("--------------------------------------------------")
        print("{:^45s}".format("Your Personal Details"))
        print("--------------------------------------------------")
        print("Your Name: %s" % sign_user)
        print("Your Address : %s" % address_user)
        #
        print("")
        cfm_sign = input("Is your personal details correct? [yes/no]: ")  # ask user if their personal details is correct

        if cfm_sign == "yes":  # if is personal details is correct
            login()  # go to login page

        else:  # if personal details is incorrect
            print("")
            print("I am so sorry.")
            print("Please try signing up again.")
            print("")
            signUp()  # go back to sign up page

    else:  # if user does not want to sign up for an account
       log_page()  # go to signup/login menu to tell user that they must sign up/login in order to go to main menu


#----------------------------------------------------------------------------------------------------------------------#
# Login Page
def login():
    print("")
    print("")
    print("Please login using your account.")
    print("--------------------------------------------------")
    print("{:^45s}".format("Login Your Account"))
    print("--------------------------------------------------")

    global user_login  # declare a global user_login variable to be used later when applicable

    user_login = input("Your registered username: ")  # ask user to enter their registered username to login
    print("")

    if user_login == sign_user:  # to check if the login username is the same as the registered username
        print("Login Successfully.")  # print this when login is successful
        print("")
        main()  # go to main menu once login successful

    else:  # if login username is not the same as the registered username / user has not registered their account yet
        print("Invalid username/Cannot Be Found.")
        print("Please try again or Sign up for an account.")
        print("")
        log_page()  # go back to signup/login page

#----------------------------------------------------------------------------------------------------------------------#
# View Menu (Display the menu items in alphabetical, price and category order)
def show_items():
    print("")
    print("View Menu")
    print("-----------------------------------")
    print("{:^35s}".format("Groceries Menu"))
    print("-----------------------------------")
    print("How do you want to view it?")
    print("")
    print("1. By Alphabetical Order")
    print("2. By Price (Lowest-Highest)")
    print("3. By Category")
    print("4. Return to Main Menu")

    print("")
    displayOption = int(input("Please enter your option (1-4): "))  # ask user to enter their option of their choice


    if displayOption == 1:  # if user chose to view by alphabetical order
        groc_alpha()  # func to show the 5 different categories for alphabet
        print("")
        which = int(input("Please enter your option (1-6): "))  # ask user which category they want to view
        print("")

        if which == 1:  # if user chose dairy
            alpha_dairy()  # func to show the items in dairy category (alphabetical order)

        elif which == 2:  # if user chose packaged goods
            alpha_packaged()  # func to show the items in packaged goods category (alphabetical order)

        elif which == 3:  # if user chose canned goods
            alpha_canned()  # func to show the items in canned goods category (alphabetical order)

        elif which == 4:  # if user chose condiments/sauces
            alpha_consauces()  # func to show the items in con/sauces category (alphabetical order)

        elif which == 5:  # if user chose drinks/beverages
            alpha_bev()  # func to show the items in drinks/bev category (alphabetical order)

        else:  # if user chose option 6
            show_items()  # func to return to groceries menu


    elif displayOption == 2:  # if user chose to view by price order
        groc_price()  # func to show the 5 different categories for price
        print("")
        which = int(input("Please enter your option (1-6): "))  # ask user which category they want view
        print("")

        if which == 1:  # if user chose dairy
            price_dairy()  # func to show the items in dairy category (price order)

        elif which == 2:  # if user chose packaged goods
            price_packaged()  # func to show the items in packaged goods category (price order)

        elif which == 3:  # if user chose canned goods
            price_canned()  # func to show the items in canned goods category (price order)

        elif which == 4:  # if user chose condiments/sauces
            price_consauces()  # func to show the items in con/sauces category (price order)

        elif which == 5:  # if user chose drinks/beverages
            price_bev()  # func to show the items in drinks/bev category (price order)

        else:  # if user chose option 6
            show_items()  # func to return to groceries menu


    elif displayOption == 3:  # if user chose to view by category order
        groc_cat() # func to show the 5 different categories for category
        print("")
        which = int(input("Please enter your option (1-6): "))  # ask user which category they want view
        print("")

        if which == 1:  # if user chose dairy
            cat_dairy()  # func to show the items in dairy category (category order)

        elif which == 2:  # if user chose packaged goods
            cat_packaged()  # func to show the items in packaged goods category (category order)

        elif which == 3:  # if user chose canned goods
            cat_canned()  # func to show the items in canned goods category (category order)

        elif which == 4:  # if user chose condiments/sauces
            cat_consauces()  # func to show the items in con/sauces category (category order)

        elif which == 5:  # if user chose drinks/beverages
            cat_bev()  # func to show the items in drinks/bev category (category order)

        else:  # if user chose option 6
            show_items()  # func to return to groceries menu

    else:
        print("")
        main()  # func to return main menu

#----------------------------------------------------------------------------------------------------------------------#
# View Menu Functions

# Sorting Functions (Alphabetical Order, By Price, By Category)
# View Category Items in Alphabetical Order
def alpha_dairy():  # Dairy
    print("")
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" ID", " Name", " Price($)"))
    print("------------------------------------------------")

    print("{:^5s}|{:<30s}|{:<25s}".format(" 1", " Biscuits", " $5.30"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 2", " Butter", " $4.50"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 3", " Cheese Slices", " $3.15"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 4", " Eggs", " $3.40"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 5", " Evaporated Milk Creamer", " $1.40"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 6", " Milk", " $2.30"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 7", " Milo", " $12.50"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 8", " Yogurt", " $0.95"))
    print("")
    alphabet()  # func to go back to the specific section (Alphabetical)

def alpha_packaged():  # Packaged Goods
    print("")
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" ID", " Name", " Price($)"))
    print("------------------------------------------------")

    print("{:^5s}|{:<30s}|{:<25s}".format(" 1", " Barley", " $1.05"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 2", " Bread", " $2.70"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 3", " Cereal", " $7.00"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 4", " Chips", " $2.60"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 5", " Crackers", " $3.10"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 6", " Green Beans", " $1.05"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 7", " Nuts", " $2.00"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 8", " Raisin", " $2.10"))
    print("")
    alphabet()  # func to go back to the specific section (Alphabetical)

def alpha_canned():  # Canned Goods
    print("")
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" ID", " Name", " Price($)"))
    print("------------------------------------------------")

    print("{:^5s}|{:<30s}|{:<25s}".format(" 1", " Baking Beans", " $1.35"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 2", " Button Mushroom", " $1.15"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 3", " Chicken Luncheon Meat", " $1.95"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 4", " Kernel Corn", " $1.25"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 5", " Pickled Lettuce", " $0.95"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 6", " Sardine Fish", " $1.10"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 7", " Tomato", " $1.45"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 8", " Tuna Fish", " $1.45"))
    print("")
    alphabet()  # func to go back to the specific section (Alphabetical)

def alpha_consauces():  # Condiments/Sauces
    print("")
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" ID", " Name", " Price($)"))
    print("------------------------------------------------")

    print("{:^5s}|{:<30s}|{:<25s}".format(" 1", " Chicken Stock", " $3.15"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 2", " Chilli Sauce", " $2.65"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 3", " Fine Salt", " $0.80"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 4", " Oyster Sauce", " $4.50"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 5", " Sea Salt Flakes", " $1.30"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 6", " Sesame Oil", " $4.95"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 7", " Sweet Soy Sauce", " $3.75"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 8", " Tomato Ketchup", " $3.20"))
    print("")
    alphabet()  # func to go back to the specific section (Alphabetical)

def alpha_bev():  # Drinks/Beverages
    print("")
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" ID", " Name", " Price($)"))
    print("------------------------------------------------")

    print("{:^5s}|{:<30s}|{:<25s}".format(" 1", " Blackcurrant Ribena 330 ML", " $31.00"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 2", " Coke 24 Cans", " $12.40"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 3", " Green Tea Canned 330 ML", " $15.00"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 4", " Mineral Water 24 x 600 ML", " $7.00"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 5", " Nescafe Coffee", " $9.90"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 6", " Orange Cordial 2 Litre", " $3.90"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 7", " Pineapple juice", " $0.80"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 8", " 100 Plus 24 Cans", " $15.00"))
    print("")
    alphabet()  # func to go back to the specific section (Alphabetical)


# View Category Items by Price (Lowest-Highest)
def price_dairy():  # Dairy
    print("")
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" ID", " Name", " Price($)"))
    print("------------------------------------------------")

    print("{:^5s}|{:<30s}|{:<25s}".format(" 1", " Yogurt", " $0.95"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 2", " Evaporated Milk Creamer", " $1.40"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 3", " Milk", " $2.30"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 4", " Cheese Slices", " $3.15"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 5", " Eggs", " $3.40"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 6", " Butter", " $4.50"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 7", " Biscuits", " $5.30"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 8", " Milo", " $12.50"))
    print("")
    price()  # func to go back to the specific section (Price)

def price_packaged():  # Packaged Goods
    print("")
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" ID", " Name", " Price($)"))
    print("------------------------------------------------")

    print("{:^5s}|{:<30s}|{:<25s}".format(" 1", " Barley", " $1.05"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 2", " Green Beans", " $1.05"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 3", " Nuts", " $2.00"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 4", " Raisin", "$2.10"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 5", " Chips", " $2.60"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 6", " Bread", " $2.70"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 7", " Crackers", " $3.10"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 8", " Cereal", " $7.00"))
    print("")
    price()  # func to go back to the specific section (Price)

def price_canned():  # Canned Goods
    print("")
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" ID", " Name", " Price($)"))
    print("------------------------------------------------")

    print("{:^5s}|{:<30s}|{:<25s}".format(" 1", " Pickled Lettuce", " $0.95"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 2", " Sardine Fish", " $1.10"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 3", " Button Mushroom", " $1.15"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 4", " Kernel Corn", " $1.25"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 5", " Baking Beans", " $1.35"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 6", " Tomato", " $1.45"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 7", " Tuna Fish", " $1.45"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 8", " Chicken Luncheon Meat", " $1.95"))
    print("")
    price()  # func to go back to the specific section (Price)

def price_consauces():  # Condiments/Sauces
    print("")
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" ID", " Name", " Price($)"))
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" 1", " Fine Salt", " $0.80"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 2", " Sea Salt Flakes", " $1.30"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 3", " Chilli Sauce", " $2.65"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 4", " Chicken Stock", " $3.15"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 5", " Tomato Ketchup", " $3.20"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 6", " Sweet Soy Sauce", " $3.75"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 7", " Oyster Sauce", " $4.50"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 8", " Sesame Oil", " $4.95"))
    print("")
    price()  # func to go back to the specific section (Price)

def price_bev():  # Drinks/Beverages
    print("")
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" ID", " Name", " Price($)"))
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" 1", " Pineapple juice", " $0.80"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 2", " Orange Cordial 2 Litre", " $3.90"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 3", " Mineral Water 24 x 600 ML", " $7.00"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 4", " Nescafe Coffee", " $9.90"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 5", " Coke 24 Cans", " $12.40"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 6", " Green Tea Canned 330 ML", " $15.00"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 7", " 100 Plus 24 Cans", " $15.00"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 8", " Blackcurrant Ribena 330 ML", " $31.00"))
    print("")
    price()  # func to go back to the specific section (Price)


# View Category Items by Category
def cat_dairy():  # Dairy
    print("")
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" ID", " Name", " Price($)"))
    print("------------------------------------------------")

    print("{:^5s}|{:<30s}|{:<25s}".format(" 1", " Milk", " $2.30"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 2", " Butter", " $4.50"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 3", " Eggs", " $3.40"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 4", " Cheese Slices", " $3.15"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 5", " Evaporated Milk Creamer", " $1.40"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 6", " Milo", " $12.50"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 7", " Biscuits", " $5.30"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 8", " Yogurt", " $0.95"))
    print("")
    cat()  # func to go back to the specific section (Category)

def cat_packaged():  # Packaged Goods
    print("")
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" ID", " Name", " Price($)"))
    print("------------------------------------------------")

    print("{:^5s}|{:<30s}|{:<25s}".format(" 1", " Bread", " $2.70"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 2", " Cereal", " $7.00"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 3", " Crackers", " $3.10"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 4", " Chips", " $2.60"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 5", " Raisin", "$2.10"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 6", " Nuts", " $2.00"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 7", " Green Beans", " $1.05"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 8", " Barley", " $1.05"))
    print("")
    cat()  # func to go back to the specific section (Category)

def cat_canned():  # Canned Goods
    print("")
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" ID", " Name", " Price($)"))
    print("------------------------------------------------")

    print("{:^5s}|{:<30s}|{:<25s}".format(" 1", " Tomato", " $1.45"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 2", " Button Mushroom", " $1.15"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 3", " Baking Beans", " $1.35"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 4", " Tuna Fish", " $1.45"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 5", " Kernel Corn", " $1.25"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 6", " Sardine Fish", " $1.10"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 7", " Chicken Luncheon Meat", " $1.95"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 8", " Pickled Lettuce", " $0.95"))
    print("")
    cat()  # func to go back to the specific section (Category)

def cat_consauces():  # Condiments/Sauces
    print("")
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" ID", " Name", " Price($)"))
    print("------------------------------------------------")

    print("{:^5s}|{:<30s}|{:<25s}".format(" 1", " Fine Salt", " $0.80"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 2", " Sea Salt Flakes", " $1.30"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 3", " Chicken Stock", " $3.15"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 4", " Chilli Sauce", " $2.65"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 5", " Oyster Sauce", " $4.50"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 6", " Sweet Soy Sauce", " $3.75"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 7", " Tomato Ketchup", " $3.20"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 8", " Sesame Oil", " $4.95"))
    print("")
    cat()  # func to go back to the specific section (Category)

def cat_bev():  # Drinks/Beverages
    print("")
    print("------------------------------------------------")
    print("{:^5s}|{:<30s}|{:<25s}".format(" ID", " Name", " Price($)"))
    print("------------------------------------------------")

    print("{:^5s}|{:<30s}|{:<25s}".format(" 1", " Green Tea Canned 330 ML", " $15.00"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 2", " Blackcurrant Ribena 330 ML", " $31.00"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 3", " 100 Plus 24 Cans", " $15.00"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 4", " Orange Cordial 2 Litre", " $3.90"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 5", " Mineral Water 24 x 600 ML", " $7.00"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 6", " Pineapple juice", " $0.80"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 7", " Nescafe Coffee", " $9.90"))
    print("{:^5s}|{:<30s}|{:<25s}".format(" 8", " Coke 24 Cans", " $12.40"))
    print("")
    cat()  # func to go back to the specific section (Category)


# This will print when user select by Alphabetical Order option
def groc_alpha():
    print("")
    print("--------------------------------------")
    print("{:^35s}".format("By Alphabetical Order"))
    print("--------------------------------------")
    print("Which category do you want to view?")
    print("")
    print("1. Dairy")
    print("2. Packaged Goods")
    print("3. Canned Goods")
    print("4. Condiments/Sauces")
    print("5. Drinks & Beverages")
    print("6. Return to Groceries Menu")


# This will print when user select by Price option
def groc_price():
    print("")
    print("--------------------------------------")
    print("{:^35s}".format("By Price (Lowest-Highest)"))
    print("--------------------------------------")
    print("Which category do you want to view?")
    print("")
    print("1. Dairy")
    print("2. Packaged Goods")
    print("3. Canned Goods")
    print("4. Condiments/Sauces")
    print("5. Drinks & Beverages")
    print("6. Return to Groceries Menu")


# This will print when user select by Category option
def groc_cat():
    print("")
    print("--------------------------------------")
    print("{:^35s}".format("By Category"))
    print("--------------------------------------")
    print("Which category do you want to view?")
    print("")
    print("1. Dairy")
    print("2. Packaged Goods")
    print("3. Canned Goods")
    print("4. Condiments/Sauces")
    print("5. Drinks & Beverages")
    print("6. Return to Groceries Menu")


# Return to Specific Section (Alphabetical, Price, Category)
# Func to go back to Alphabet based
def alphabet():
    back = int(input("Enter 0 to view Groceries Menu by Alphabetical Order: "))  # user to enter 0 to go back to Alphabetical section groceries menu

    if back == 0:  # if user entered 0
        groc_alpha()  # func to show the 5 categories under alphabet based section

        print("")
        which = int(input("Please enter your option (1-6): "))   # user to enter their option
        print("")

        if which == 1:  # if user chose dairy
            alpha_dairy()  # func to show the items in dairy category (alphabetical order)

        elif which == 2:  # if user chose packaged goods
            alpha_packaged()  # func to show the items in packaged goods category (alphabetical order)

        elif which == 3:  # if user chose canned goods
            alpha_canned()  # func to show the items in canned goods category (alphabetical order)

        elif which == 4:  # if user chose condiments/sauces
            alpha_consauces()  # func to show the items in con/sauces category (alphabetical order)

        elif which == 5:  # if user chose drinks/beverages
            alpha_bev()  # func to show the items in drinks/bev category (alphabetical order)

        else:  # if user chose option 6
            show_items()  # func to return to groceries menu

    else:  # if option is not 0
        main()  # func to return to main menu


# Func to go back to Price based
def price():
    back = int(input("Enter 0 to continue view Groceries Menu by Price (Lowest-Highest): "))  # user to enter 0 to go back to Price section groceries menu

    if back == 0:  # if user entered 0
        groc_price()  # func to show the 5 categories under price based section

        print("")
        which = int(input("Please enter your option (1-6): "))  # user to enter their option
        print("")

        if which == 1:  # if user chose dairy
            price_dairy()  # func to show the items in dairy category (price order)

        elif which == 2:  # if user chose packaged goods
            price_packaged()  # func to show the items in packaged goods category (price order)

        elif which == 3:  # if user chose canned goods
            price_canned()  # func to show the items in canned goods category (price order)

        elif which == 4:  # if user chose condiments/sauces
            price_consauces()  # func to show the items in con/sauces category (price order)

        elif which == 5:  # if user chose drinks/beverages
            price_bev()  # func to show the items in drinks/bev category (price order)

        else:  # if user chose option 6
            show_items()  # func to return to groceries menu

    else:  # if option is not 0
        main()  # func to return to main menu


# Func to go back to Category based
def cat():
    back = int(input("Enter 0 to continue view Groceries Menu by Category: "))  # user to enter 0 to go back to Category section groceries menu

    if back == 0:  # if user entered 0
        groc_cat()  # func to show the 5 categories under category based section
        print("")

        which = int(input("Please enter your option (1-6): "))  # user to enter their option
        print("")

        if which == 1:  # if user chose dairy
            cat_dairy()  # func to show the items in dairy category (category order)

        elif which == 2:  # if user chose packaged goods
            cat_packaged()  # func to show the items in packaged goods category (category order)

        elif which == 3:  # if user chose canned goods
            cat_canned()  # func to show the items in canned goods category (category order)

        elif which == 4:  # if user chose condiments/sauces
            cat_consauces()  # func to show the items in con/sauces category (category order)

        elif which == 5:  # if user chose drinks/beverages
            cat_bev()  # func to show the items in drinks/bev category (category order)

        else:  # if user chose option 6
            show_items()  # func to return to groceries menu

    else:  # if option is not 0
        main()  # func to return to main menu

#----------------------------------------------------------------------------------------------------------------------#
# Place Orders
def add_items():
    print("")
    print("Place Orders")
    print("-------------------------------")
    print("{:^30s}".format("Groceries Categories"))
    print("-------------------------------")
    print("1. Dairy")
    print("2. Packaged Goods")
    print("3. Canned Goods")
    print("4. Condiments/Sauces")
    print("5. Drinks & Beverages")
    print("6. Return to Main Menu")

    global menu_items  # declare menu_items as global variable to be used in other functions
    global menu_category  # declare menu_category as global variable to be used in other functions
    global subtotal  # declare subtotal as global variable to be used in other functions
    global quantity  # declare quantity as global variable to be used in other functions

    menu_category = []  # to append category to an empty menu_category list
    menu_items = []  # to append items to an empty menu_items list

    for key in dictItems:  # to get the key (category) from dictItems
        menu_category.append(key)  # append the key (category) into the empty menu_category list
    print("")

    global option1  # declare option1 as global variable to be used in other functions

    option1 = int(input("Please choose a Category (1-{}), 6 to return Main Menu: ".format(len(menu_category)))) # allow user to enter a category (1-5) from the appended menu_category list
    print("")

    if option1 > 0 and option1 <= len(dictItems):  # if the category user entered is (1 to 5)
        category = menu_category[option1-1]  # create a category variable for the selection of items user chose from the category

        print("-------------------------------------------------------")
        menu_items = dictItems.get(category)  # to fetch all the items from category in the dictionary into menu_items list
        print("{:^5s}|{:<30s}|{:<25s}".format("ID", "Items", "Price($)"))
        print("-------------------------------------------------------")

        for i in range(len(menu_items)):  # to print all the items (id, items, and price) of the user chosen category
            print("{:^5d}|{:<30s}|{:<25.2f}".format(i+1, menu_items[i][0], menu_items[i][1]))
        print("")

        global choice  # declare choice as global variable to be used in other functions

        # allow user to choose any of the 8 items from the menu_items list
        choice = int(input("Please select an item to buy (1-{}), 0 to return to Place Order: ".format(len(menu_items))))

        if choice == 0:  # if user enter number 0
            print("")
            add_items()  # func to return to place order

        else:  # if user enter number between (1 to 8)
            quantity = int(input("Please select your quantity: "))  # allow user to enter the quantity they want
            print("")
            print("")

            if quantity > 0:  # if the quantity user enter is more than 0
                subtotal = quantity*menu_items[choice-1][1]  # calculate the total price of the items chosen with number of quantity included


                print("--------------------------------------------------------------------------------------------------------------------")
                print("{:^115}".format("Item Selected:"))
                print("--------------------------------------------------------------------------------------------------------------------")
                print("{:^5s}|{:<25s}|{:<30s}|{:<25s}|{:<15s}|{:<15s}".format("ID", "Category", "Items", "Price($)", "Quantity", "SubTotal($)"))
                print("--------------------------------------------------------------------------------------------------------------------")

                print("{:^5d}|{:<25s}|{:<30s}|{:<25.2f}|{:<15d}|{:<15.2f}".format(choice, menu_category[option1-1], menu_items[choice-1][0], menu_items[choice-1][1],
                                                                        quantity, subtotal))  # to show the orders that user placed /
                                                    # to print the user chosen item with quantity and subtotal
                print("")

                confirm = input("Do you want to add this item to cart? [yes/no]: ")  # to ask the user if they want to add their items to cart

                if confirm == "yes":  # if the user want to add their items to cart
                    listID.append(choice)  # append the id of items user chosen into listID
                    categoryList.append(menu_category[option1-1])  # append category user chosen into categoryList
                    cartList.append(menu_items[choice-1][0])  # append items into cartList
                    unitpriceList.append(menu_items[choice-1][1])  # append the unit price of items in unitpriceList
                    quantityList.append(quantity)  # append the quantity user selected in quantityList
                    subList.append(subtotal)  # append the subtotal of the items in subList

                    # to check if all of the data is printed
                    # print(listID)
                    # print(categoryList)
                    # print(cartList)
                    # print(unitpriceList)
                    # print(quantityList)
                    # print(subList)

                    print("Order placed successfully.")
                    print("")
                    print("")

                    # to print the items user had selected
                    print("--------------------------------------------------------------------------------------------------------------------")
                    print("{:^115}".format("Your Purchase Items:"))
                    print("--------------------------------------------------------------------------------------------------------------------")
                    print("{:^5s}|{:<25s}|{:<30s}|{:<25s}|{:<15s}|{:<15s}".format("ID", "Category", "Items", "Price($)", "Quantity", "SubTotal($)"))
                    print("--------------------------------------------------------------------------------------------------------------------")

                    for i in range(len(cartList)):  # to show the items user had placed currently and previously
                        # to show the orders that user placed / # to print the user chosen item with quantity and subtotal
                        print("{:^5d}|{:<25s}|{:<30s}|{:<25.2f}|{:<15d}|{:<15.2f}".format(i+1, categoryList[i], cartList[i], unitpriceList[i], quantityList[i], subList[i]))
                        print("")

                    option2 = input("Do you want to add new items? [yes/no]: ")  # ask user if they want to add more items into the cart

                    if option2 == "yes": # if user want to add items again
                        add_items()  # func to go back to place order
                        listID.append(choice)  # append the id of items user chosen into listID
                        categoryList.append(menu_category[option1-1])  # append category user chosen into categoryList
                        cartList.append(menu_items[choice-1][0])  # append items user chosen into cartList
                        unitpriceList.append(menu_items[choice-1][1])  # append the unit price of items chosen in unitpriceList
                        quantityList.append(quantity)  # append the quantity user selected in quantityList
                        subList.append(subtotal)  # append the subtotal of the items in subList

                        # to check if all of the data is printed
                        # print(listID)
                        # print(categoryList)
                        # print(cartList)
                        # print(unitpriceList)
                        # print(quantityList)
                        # print(subList)

                        print("")
                        print("Order placed successfully.")
                        print("")

                    else:  # if the user does not want to continue adding items
                        print("Alright, it's okay :/")
                        print("")
                        main()  # func to return to main menu

                else:  # if user does not want to add to cart
                    print("")
                    main()  # func to return to main menu

            else:  # if quantity is less than 0
                print("Invalid Selection")
                add_items()  # func to go back to place order

    else:  # if category chosen is not between (1 to 5)
        print("Invalid Selection")
        main()  # func to go back to main menu

#----------------------------------------------------------------------------------------------------------------------#
# View Orders
def view_items():
    # to print all the items user had selected
    print("")
    print("View Orders Placed")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("{:^115}".format("Your Shopping Cart:"))
    print("--------------------------------------------------------------------------------------------------------------------")
    print("{:^5s}|{:<25s}|{:<30s}|{:<25s}|{:<15s}|{:<15s}".format("ID", "Category", "Items", "Price($)", "Quantity", "SubTotal($)"))
    print("--------------------------------------------------------------------------------------------------------------------")

    for i in range(len(cartList)):  # to show all the items user had placed currently and previously
        print("{:^5d}|{:<25s}|{:<30s}|{:<25.2f}|{:<15d}|{:<15.2f}".format(i+1, categoryList[i], cartList[i], unitpriceList[i], quantityList[i], subList[i]))  # to show the orders that user placed / # to print the user chosen item with quantity and subtotal
        print("")

#----------------------------------------------------------------------------------------------------------------------#
# Remove Existing Items
def remove_items():
    # to print all the items user had selected
    print("")
    print("Remove Existing Orders")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("{:^115}".format("Your Shopping Cart:"))
    print("--------------------------------------------------------------------------------------------------------------------")
    print("{:^5s}|{:<25s}|{:<30s}|{:<25s}|{:<15s}|{:<15s}".format("ID", "Category", "Items", "Price($)", "Quantity", "SubTotal($)"))
    print("--------------------------------------------------------------------------------------------------------------------")

    for i in range(len(cartList)):  # to show all the items user had placed currently and previously
        print("{:^5d}|{:<25s}|{:<30s}|{:<25.2f}|{:<15d}|{:<15.2f}".format(i+1, categoryList[i], cartList[i], unitpriceList[i], quantityList[i], subList[i]))  # to show the orders that user placed / # to print the user chosen item with quantity and subtotal
        print("")

    delete = int(input('Enter the item ID you want to remove, 0 to return to Main Menu: '))  # ask user to enter items they want to remove
    print("")

    if delete == 0:  # if user enter 0
        print("")
        main()  # func to return main menu

    else:
        for i in range(len(cartList)):  # to show the items user wants to delete
            print("")
            print("")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("{:^115}".format("Items Chosen to Delete:"))
            print("--------------------------------------------------------------------------------------------------------------------")
            print("{:^5s}|{:<25s}|{:<30s}|{:<25s}|{:<15s}|{:<15s}".format("ID", "Category", "Items", "Price($)", "Quantity", "SubTotal($)"))
            print("--------------------------------------------------------------------------------------------------------------------")
            print("{:^5d}|{:<25s}|{:<30s}|{:<25.2f}|{:<15d}|{:<15.2f}".format(delete, categoryList[delete-1], cartList[delete-1], unitpriceList[delete-1], quantityList[delete-1], subList[delete-1]))  # to show the orders that user deleted
            print("")

            rem = input("Are you sure you want to remove this item? [yes/no]: ")  # ask user if they want to delete the item

            if rem == "yes":  # if user want to remove item
                catRemove = categoryList[delete-1]  # create variable to contain the category user want to delete
                itemRemove = cartList[delete-1]  # create variable to contain the item user want to delete
                priceRemove = unitpriceList[delete-1]  # create variable to contain the price of items of user delete selection
                quantRemove = quantityList[delete-1]  # create variable to contain the quantity of items of user delete selection
                subRemove = subList[delete-1]  # create variable to contain the subtotal of items of user delete selection
                categoryList.remove(catRemove)  # to remove the category items user want to delete from categoryList
                cartList.remove(itemRemove)  # to remove the item user want to delete from cartList
                unitpriceList.remove(priceRemove)  # to remove the unitprice of items user want to delete from unitpriceList
                quantityList.remove(quantRemove)  # to remove the quantity of items user want to delete from quantityList
                subList.remove(subRemove)  # to remove the subtotal of items from subList

                # to check which items was removed
                # print(catRemove)
                # print(itemRemove)
                # print(priceRemove)
                # print(quantRemove)
                # print(subRemove)

                # to check what items was left in the cart
                # print(cartList)
                # print(categoryList)
                # print(unitpriceList)
                # print(quantityList)
                # print(subList)

                print('Items successfully removed.')
                print("")
                print("")

                # to print all the items user had in shopping cart
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("{:^115}".format("Your Shopping Cart:"))
                print("--------------------------------------------------------------------------------------------------------------------")
                print("{:^5s}|{:<25s}|{:<30s}|{:<25s}|{:<15s}|{:<15s}".format("ID", "Category", "Items", "Price($)", "Quantity", "SubTotal($)"))
                print("--------------------------------------------------------------------------------------------------------------------")

                for i in range(len(cartList)):  # to show the remaining items user had left in cart
                    print("{:^5d}|{:<25s}|{:<30s}|{:<25.2f}|{:<15d}|{:<15.2f}".format(i+1, categoryList[i], cartList[i], unitpriceList[i], quantityList[i], subList[i])) #updated list after removing items
                    print("")

                print("")
                remove_again = input("Do you want to continue to remove items? [yes/no]: ")  # ask user if they want to continue removing the items

                if remove_again == "yes":  # if user want to remove again
                    remove_items() # loop back to remove again
                    catRemove = categoryList[delete-1]  # create variable to contain the category user want to delete
                    itemRemove = cartList[delete-1]  # create variable to contain the item user want to delete
                    priceRemove = unitpriceList[delete-1]  # create variable to contain the price of items of user delete selection
                    quantRemove = quantityList[delete-1]  # create variable to contain the quantity of items of user delete selection
                    subRemove = subList[delete-1]  # create variable to contain the subtotal of items of user delete selection
                    categoryList.remove(catRemove)  # to remove the category items user want to delete from categoryList
                    cartList.remove(itemRemove)  # to remove the item user want to delete from cartList
                    unitpriceList.remove(priceRemove)  # to remove the unitprice of items user want to delete from unitpriceList
                    quantityList.remove(quantRemove)  # to remove the quantity of items user want to delete from quantityList
                    subList.remove(subRemove) # to remove the subtotal of items from subList

                    # # to check which items was removed
                    # print(catRemove)
                    # print(itemRemove)
                    # print(priceRemove)
                    # print(quantRemove)
                    # print(subRemove)
                    #
                    # # to check what items was left in the cart
                    # print(cartList)
                    # print(categoryList)
                    # print(unitpriceList)
                    # print(quantityList)
                    # print(subList)

                else:  # if user do not want to remove again
                    print('Thank You.')
                    print('')
                    main()  # func to go back to main menu

            else:  # if user do not want to remove item
                print("Thank You.")
                print("")
                main()  # func to go back to main menu

#----------------------------------------------------------------------------------------------------------------------#
# Payment/CheckOut

discount = 10  # discount
gst = 7  # gst

def payment_checkout():  # func for payment checkout
    global final
    totalCost = sum(subList)  # total price of items
    gstCost = subtotal * (gst/100)  # gst price
    priceGst = totalCost + gstCost  # total price inclusive of gst
    priceDisc = totalCost - totalCost * (discount/100)  # price with discount
    final = gstCost + priceDisc  # final price inclusive of disc and gst

    # print the order bill summary
    print("--------------------------------------------------------------")
    print("{:^60s}".format("Order Bill Summary"))
    print("--------------------------------------------------------------")
    print("{:<30s}|{:<15s}|{:<15s}".format("Items", "Quantity", "SubTotal($)"))
    print("--------------------------------------------------------------")

    for i in range(len(cartList)):  # to show list of items to pay
        print("{:<30s}|{:<15d}|{:<15.2f}".format(cartList[i], quantityList[i], subList[i]))
        print("")

    print("Total Price of Items: ${:.2f}".format(totalCost))  # print the total price of items
    print("Inclusive of 7% GST: ${:.2f}".format(priceGst))  # print the total price inclusive of gst
    print("With 10% discount: ${:.2f}".format(priceDisc))  # print the 10% discounted price
    print("Final Payment Amount (incl. GST & Discount): ${:.2f}".format(final))  # print the final payment amount
    print("")

    checkout = input('Would you like to check out? [yes/no]: ')  # ask user if they want to confirm checkout
    print("")

    if checkout == 'yes':  # if user option is yes
        print("-------------------------------------")
        print("{:^35s}".format("Checkout"))
        print("-------------------------------------")
        print("1. Proceed to Payment")
        print("2. Return Main Menu")
        print("")

        pay = int(input("Enter your option (1-2): "))  # user to enter option
        print("")

        if pay == 1:  # if user chose option 1
            payment_method()  # func for payment methods

        else:  # if user chose option 2
            print("--------------------------------------------------------------")
            print("")
            print("{:^65s}".format("Thank You for shopping with Triple Ins :))"))
            print("{:^65s}".format("Please come again!"))
            print("")
            print("--------------------------------------------------------------")
            print("")
            main()  # func to return main menu

    else:
        print("")
        main()  # func to return main menu


def payment_method():  # func for payment method
    # print the 5 payment methods

    global paymentList  # declare paymentList as global variable to be used later when necessary
    global paymentMethod  # declare paymentMethod as global variable to be used later when necessary
    global payment_type  # declare payment_type as global variable to be used later when necessary

    paymentList = ["Credit Card", "Debit Card", "PayLah", "VISA", "Paypal"]

    print("-------------------------------------")
    print("{:^35s}".format("Payment Methods"))
    print("-------------------------------------")
    print("How do you want to pay by?")
    print("")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. PayLah")
    print("4. VISA")
    print("5. Paypal")
    print("")

    paymentMethod = input("How would you like to make your payment? ")  # ask user how they want to make payment
    print("")

    if paymentMethod == "1":  # pay by credit card
        payment_type = paymentList[0]
        paybycards()  # func to pay by cards

    elif paymentMethod == "2":  # pay by debit card
        payment_type = paymentList[1]
        paybycards()  # func to pay by cards

    elif paymentMethod == "3":  # pay by PayLah
        payment_type = paymentList[2]
        phone_no = int(input("Please enter your phone number: "))  # enter phone number
        print("")
        print("Your phone number:", phone_no)
        cfm_phoneNo = input("Are you sure this is your phone number? [yes/no]: ")  # ask user if this is their phone number

        if cfm_phoneNo == "yes":  # if is their phone number
            paymentSuccessful()  # func for payment successful

        else:
            print("")
            print("Please ensure your phone number is entered correctly.")
            print("")
            payment_method()  # func for payment method

    elif paymentMethod == "4":  # pay by visa
        payment_type = paymentList[3]
        paybycards()

    elif paymentMethod == "5":  #pay by paypal
        payment_type = paymentList[4]
        email = input("Please enter your email: ")
        print("")
        print("Your email:", email)
        cfm_email = input("Are you sure this is your email? [yes/no]: ")  # ask user if this is their email

        if cfm_email == "yes":  # if email is theirs
          paymentSuccessful()  # func for payment successful

        else:
          print("")
          print("Please ensure your email is entered correctly.")
          print("")


def paybycards():  # func to pay by cards
    global card_no  # declare a global card_no variable to use later when necessary
    card_no = input("Please enter your card number: ")  # enter credit card number
    print("")
    print("Your credit card number:", card_no)  # print credit card number
    cfm_cardNo = input("Are you sure this is your card number? [yes/no]: ")  # confirm credit number

    if cfm_cardNo == "yes":  # if credit card is confirmed
        paymentSuccessful()   # func for payment successful

    else:
        print("")
        print("Please ensure your card number is entered correctly.")
        print("")
        payment_method()  # func for payment_method


# func for payment successful
def paymentSuccessful():
    print("")
    print("-------------------------------------------------------------------")
    print("")
    print("{:^67s}".format("Payment Successful!"))
    print("{:^67s}".format("Items will be shipped to: %s" % address_user))
    print("{:^67s}".format("Please verify your confirmation in your email."))
    print("")
    print("{:^67s}".format("Thank You for shopping with Triple Ins Grocery :))"))
    print("{:^67s}".format("Please come again!"))
    print("")
    print("-------------------------------------------------------------------")
    print("Your items will be delivered to your doorstep in 1 week.")
    print("Please be patient, we'll make every effort to ensure that your groceries are delivered in perfect condition!")
    print("If there are any damages or frauds, please kindly inform us and show the receipt if you would prefer a refund or replacement.")
    print("")

    receipt = input("Do you want your receipt? [yes/no] ")  # ask if the user wants receipt
    print("")

    if receipt == "yes":  # if user wants receipt
        user_receipt()

    else:  # if user does not want receipt
        print("Thank you. Please come again!")
        print("")
        feedback_form()

def user_receipt():  # func for receipt
    print("")
    print("--------------------------------------------------------------")
    print("{:^58s}".format("TRIPLE INS' GROCERY"))
    print("{:^58s}".format("Tel: 8537 0971"))
    print("--------------------------------------------------------------")
    print("{:^57s}".format("Cash Receipt"))
    print("--------------------------------------------------------------")
    print("{:<30s}|{:<15s}|{:<15s}".format("Items", "Quantity", "SubTotal($)"))
    print("--------------------------------------------------------------")

    for i in range(len(cartList)):   # to show list of items on receipt
      print("{:<30s}|{:<15d}|{:<15.2f}".format(cartList[i], quantityList[i], subList[i]))
    print("")
    print("--------------------------------------------------------------")
    print("TOTAL: ${:.2f}".format(final))  # print total price
    print("GST 7%")
    print("--------------------------------------------------------------")
    print("Payment by:", payment_type)  # print payment method
    print("---------------------------------------------------------------")
    print("{:60s}".format("THANK YOU!"))
    print("")
    print("")

    feedback_form()

#----------------------------------------------------------------------------------------------------------------------#
# Feedback
def feedback_form():

    feedback = input("Do you want to leave us some review? [yes/no]: ")  # ask user if they want to leave feedback
    print("")

    if feedback == "yes":  # if user want to leave feedback
        print("-----------------------------------")
        print("{:^35s}".format("Leave us a review 0.0"))
        print("-----------------------------------")

        global enter_feedback  # declare enter_feedback as global variable to be used later when necessary
        global enter_ratings  # declare enter_ratings as global variable to be used later when necessary

        enter_feedback = input("Your review: ")  # user to enter their feedback
        enter_ratings = int(input("Your star ratings (0-10): "))  # user to enter the ratings they would like to give
        print("")

        cfm_feedback = input("Are you sure you want to submit this review? [yes/no]: ")  # ask user if they want to submit the review

        if cfm_feedback == "yes":  # if leaving feedback is confirmed
            # print the message from Triple Ins' Grocery
            print("")
            print("Feedback sent successfully to Triple Ins' Grocery.")
            # print("")
            print("---------------------------------------------------------------------")
            # print("")
            print("%s, thanks for leaving us a feedback." % sign_user)
            # print("")
            print("We believed that we could continue to improve our service for you.")
            print("---------------------------------------------------------------------")
            print("")
            exit()

        else:  # if leaving feedback is not confirmed
            main()

    else:
        exit()  # go back to main menu

main()
