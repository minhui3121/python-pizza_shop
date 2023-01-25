# Student name: Minhui Roh
# McGill ID: 261120462

PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED = 4.0
PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED = 3.0
SPECIAL_INGREDIENT = "guacamole"
SPECIAL_INGREDIENT_COST = 19.99
FAIR = True

def get_pizza_area(diameter):
    """ (float) -> float
    Returns the area of pizza with diameter of local variable diameter
    
    >>> round(get_pizza_area(1.5), 2)
    1.77
    >>> round(get_pizza_area(4.0), 3)
    12.566
    >>> round(get_pizza_area(2.5), 4)
    4.9087
    """
    from math import pi 
    area = (diameter/2)**2 * pi
    return area
     

def get_fair_quantity(diameter1, diameter2):
    """ (float,float) -> int
    Takes two floats diameter 1 and diameter 2 for two pizzas and return how many small pizzas
    it needs to match the size of large pizza in integer.
    
    >>> get_fair_quantity(14.0, 8.0)
    4
    >>> get_fair_quantity(3.0, 11.0)
    14
    >>> get_fair_quantity(5.0, 5.0)
    1
    """
    area_pizza_1 = get_pizza_area(diameter1)
    area_pizza_2 = get_pizza_area(diameter2)
    if area_pizza_1 >= area_pizza_2:
        if area_pizza_1 % area_pizza_2 == 0:
            fair_quantity = int(area_pizza_1 / area_pizza_2)
        else:
            fair_quantity = int(area_pizza_1 / area_pizza_2 + 1)
    else:
        if area_pizza_2 % area_pizza_1 == 0:
            fair_quantity = int(area_pizza_2 / area_pizza_1)
        else:
            fair_quantity = int(area_pizza_2 / area_pizza_1 + 1)
    
    if FAIR == False:
        return int(fair_quantity * 1.5)
    else:
        return fair_quantity

def pizza_formula (d_large, d_small, c_large, c_small, n_small):
    """ (num,num,num,num,int) -> float
    Takes four floats d_large (diameter large pizza), d_small (diameter small pizza),
    c_large (cost large pizza), c_small (cost small pizza) and one integer n_small (number of small pizza).
    However, one of the floats might be -1 (int).
    Calculate the "missing" value marked by -1 using logic area/dollar large equal to
    area/dollar small and return the value as float rounded to two decimal places.
    
    >>> pizza_formula (12.0, 6.0, 10.0, -1, 2)
    5.0
    >>> pizza_formula (6.0, 5.0, 6.0, 5.0, -1)
    1.2
    >>> pizza_formula (8.0, 5.0, 12.0, -1, 3)
    14.06
    >>> pizza_formula (-1, 3.0, 10.0, 8.0, 2)
    4.74
    """
    from math import sqrt
    if d_large == -1:
        return round (2 * sqrt (c_large*(((d_small/2)**2)* n_small) / c_small), 2)
    elif d_small == -1:
        return round ((2 * sqrt ((d_large / 2)**2 * c_small / (c_large * n_small))), 2)
    elif c_large == -1:
        return round ((c_small * ((d_large/2)**2)) / (n_small * ((d_small/2)**2)), 2)
    elif c_small == -1:
        return round ((c_large * n_small * ((d_small/2)**2)) / ((d_large/2)**2),2)
    else:
        return round ((c_small * ((d_large/2)**2)) / (c_large*((d_small/2)**2)), 2)
    
def get_pizza_cake_cost(base_diameter, height_per_level):
    """ (int, float) -> float
    Takes one positive integer (base_diameter) and one positive float (height_per_level)
    and return the cost of pizza cake as a float rounded to two decimal places
    
    >>> get_pizza_cake_cost(2, 1.0)
    15.71
    >>> get_pizza_cake_cost(4, 2.0)
    188.5
    >>> get_pizza_cake_cost(7, 2.5)
    1099.56
    """
    cost = 0
    while base_diameter >= 1:
        cost=cost+get_pizza_area(base_diameter)*height_per_level*PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED
        base_diameter -= 1
    if FAIR == False:
        return round(cost * 1.5, 2)
    else:
        return round(cost, 2)

def get_pizza_poutine_cost(diameter, height):
    """ (int, float) -> float
    Takes one positive integer diameter (diameter of the poutine cylindrical cup)
    and one positive float height (height in centimeteres) and returns the cost of
    pizza poutine as a float with two decimal places.
    
    >>> get_pizza_poutine_cost(2, 1.0)
    9.42
    >>> get_pizza_poutine_cost(3, 2.0)
    42.41
    >>> get_pizza_poutine_cost(5, 2.5)
    147.26
    """
    
    pizza_poutine_cost = get_pizza_area(diameter)*height*PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED
    if FAIR == False:
        return round(pizza_poutine_cost*1.5, 2)
    else:
        return round(pizza_poutine_cost, 2)

def display_welcome_menu():
    """ () -> NoneType
    Takes no inputs and returns nothing. Displays welcome message and three options
    that a user can choose.
    
    >>> display_welcome_menu()
    Welcome To The Best Pizza Place. Our Pizzas Made With 100% Real Pizza.
    Please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    """
    print("Welcome To The Best Pizza Place. Our Pizzas Made With 100% Real Pizza.")
    print("Please choose an option:")
    print("A. Special Orders")
    print("B. Formula Mode")
    print("C. Quantity Mode")
    
def special_orders():
    """ () -> NoneType
    Takes no inputs and returns nothing.
    Let user to choose between cake and poutine, to choose their diameter and height, to choose
    the special ingredient, then display the cost of the order.
    
    >>> special_orders()
    Would you like the cake or poutine? cake
    Enter diameter: 2
    Enter height: 1.0
    Do you want the guacamole? yes
    The cost is $35.7
    >>> special_orders()
    Would you like the cake or poutine? cake
    Enter diameter: 4
    Enter height: 2.0
    Do you want the guacamole? no
    The cost is $188.5
    >>> special_orders()
    Would you like the cake or poutine? poutine
    Enter diameter: 3
    Enter height: 2.0
    Do you want the guacamole? y
    The cost is $62.4
    """
    cake_poutine = input("Would you like the cake or poutine? ")
    diameter = int(input("Enter diameter: "))
    height = float(input("Enter height: "))
    guacamole_or_no = input("Do you want the " + SPECIAL_INGREDIENT + "? ")
    if cake_poutine == "cake":
        if guacamole_or_no == "y" or guacamole_or_no == "yes":
            total_cost = round((get_pizza_cake_cost(diameter, height) + SPECIAL_INGREDIENT_COST),2)
        else:
            total_cost = round((get_pizza_cake_cost(diameter, height)), 2)
    if cake_poutine == "poutine":
        if guacamole_or_no == "y" or guacamole_or_no == "yes":
            total_cost = round((get_pizza_poutine_cost(diameter, height)+SPECIAL_INGREDIENT_COST), 2)
        else:
            total_cost = round((get_pizza_poutine_cost(diameter, height)), 2)
    print ("The cost is $" + str(total_cost))

def quantity_mode():
    """ () -> NoneType
    Takes no input and returns nothing.
    Let user input two diameters for two pizzas and display how many small pizza it needs to match
    the size of one large pizza.
    
    >>> quantity_mode()
    Enter diameter 1: 14.0
    Enter diameter 2: 8.0
    You should buy 4 pizzas.
    >>> quantity_mode()
    Enter diameter 1: 3
    Enter diameter 2: 11.0
    You should buy 14 pizzas.
    >>> quantity_mode()
    Enter diameter 1: 5.0
    Enter diameter 2: 5
    You should buy 1 pizza.
    """
    diameter1 = float(input("Enter diameter 1: " ))
    diameter2 = float(input("Enter diameter 2: " ))
    fair_quantity = get_fair_quantity(diameter1, diameter2)
    if fair_quantity == 1:
        print("You should buy " + str(fair_quantity) + " pizza.")
    else:
        print("You should buy " + str(fair_quantity) + " pizzas.")

def formula_mode():
    """ () -> NoneType
    Takes no input and returns nothing.
    Let user input diameter of large and small pizza, their respective cost, and the number of small pizza.
    One of the values will be -1 and this function prints out the real value marked by -1.
    
    >>> formula_mode()
    Enter large diameter: 12.0
    Enter small diameter: 6.0
    Enter large price: 10.0
    Enter small price: -1
    Enter small number: 2
    The missing value is: 5.0
    >>> formula_mode()
    Enter large diameter: 6.0
    Enter small diameter: 5.0
    Enter large price: 6.0
    Enter small price: 5.0
    Enter small number: -1
    The missing value is: 1.2
    >>> formula_mode()
    Enter large diameter: 8.0
    Enter small diameter: 5.0
    Enter large price: 12.0
    Enter small price: -1
    Enter small number: 3
    The missing value is: 14.06
    """
    d_large = float(input("Enter large diameter: "))
    d_small = float(input("Enter small diameter: "))
    c_large = float(input("Enter large price: "))
    c_small = float(input("Enter small price: "))
    n_small = int(input("Enter small number: "))
    print("The missing value is: " + str(pizza_formula(d_large, d_small, c_large, c_small, n_small)))
    
def run_pizza_calculator():
    """ () -> NoneType
    Takes no input and returns nothing.
    Displays a welcome message and the choice of program options, then calls the appropriate function
    depending on user input. If the input is invalid, prints out "Invalid mode."
    
    >>> run_pizza_calculator()
    Welcome To The Best Pizza Place. Our Pizzas Made With 100% Real Pizza.
    Please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: A
    Would you like the cake or poutine? cake
    Enter diameter: 2
    Enter height: 1.0
    Do you want the guacamole? yes
    The cost is $35.7
    
    >>> run_pizza_calculator()
    Welcome To The Best Pizza Place. Our Pizzas Made With 100% Real Pizza.
    Please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: B
    Enter large diameter: 12.0
    Enter small diameter: 6.0
    Enter large price: 10.0
    Enter small price: -1
    Enter small number: 2
    The missing value is: 5.0
    
    >>> run_pizza_calculator()
    Welcome To The Best Pizza Place. Our Pizzas Made With 100% Real Pizza.
    Please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: D
    Invalid mode.
    """
    if FAIR == False:
        print("HEY EVERY !! EV3RY BUDDY 'S FAVORITE [Pizza Shop]")
        print("HURRY UP AND BUY! I JUST NEED YOUR [Account Details] AND THE [Number on theB4ck]!")
        print("YUM YUM GREAT OPTIONS")
        print("A. [Specil Deals]")
        print("B. [Prize Winning] F0RMULA")
        print("C. HOW MUCH TO BUY?? [You Can Never Buy Enough]!!")
        choice = input("TAKE AN OPTION: ")
        if choice == "A":
            special_orders()
        elif choice == "B":
            formula_mode()
        elif choice == "C":
            quantity_mode()
        else:
            print("Invalid mode.")
    else:
        display_welcome_menu()
        choice = input("Your choice: ")
        if choice == "A":
            special_orders()
        elif choice == "B":
            formula_mode()
        elif choice == "C":
            quantity_mode()
        else:
            print("Invalid mode.")
            
            
    



        
    
    




    
         

    

    
    