"""
Functions necessary for running a virtual cookie shop.
See README.md for instructions.
Do not run this file directly.  Rather, run main.py instead.
"""
import csv

def bake_cookies(filepath):
    """
    Opens up the CSV data file from the path specified as an argument.
    - Each line in the file, except the first, is assumed to contain comma-separated information about one cookie.
    - Creates a dictionary with the data from each line.
    - Adds each dictionary to a list of all cookies that is returned.

    :param filepath: The path to the data file.
    :returns: A list of all cookie data, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    cookies = []

    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'].replace('$', ''))
            cookies.append(row)

    return cookies


def welcome():
    """
    Prints a welcome message to the customer in the format:

      Welcome to the Python Cookie Shop!
      We feed each according to their need.

    """
    # write your code for this function below this line
    print('Welcome to the Python Cookie Shop!')
    print('We feed each according to their need.')


def display_cookies(cookies):
    """
    Prints a list of all cookies in the shop to the user.
    - Sample output - we show only two cookies here, but imagine the output continues for all cookiese:
        Here are the cookies we have in the shop for you:

          #1 - Basboosa Semolina Cake
          This is a This is a traditional Middle Eastern dessert made with semolina and yogurt then soaked in a rose water syrup.
          Price: $3.99

          #2 - Vanilla Chai Cookie
          Crisp with a smooth inside. Rich vanilla pairs perfectly with its Chai partner a combination of cinnamon ands ginger and cloves. Can you think of a better way to have your coffee AND your Vanilla Chai in the morning?
          Price: $5.50

    - If doing the extra credit version, ask the user for their dietary restrictions first, and only print those cookies that are suitable for the customer.

    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below this line
    print("Here are the cookies we have in the shop for you:\n")
    for index, cookie in enumerate(cookies, start=1):
        print(f"  #{index} - {cookie['title']}")
        print(f"  {cookie['description']}")
        print(f"  Price: ${cookie['price']:.2f}\n")

def get_cookie_from_dict(id, cookies):
    """
    Finds the cookie that matches the given id from the full list of cookies.

    :param id: the id of the cookie to look for
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: the matching cookie, as a dictionary
    """
    # write your code for this function below this line
    return cookies[id-1]




def solicit_quantity(id, cookies):
    """
    Asks the user how many of the given cookie they would like to order.
    - Validates the response.
    - Uses the get_cookie_from_dict function to get the full information about the cookie whose id is passed as an argument, including its title and price.
    - Displays the subtotal for the given quantity of this cookie, formatted to two decimal places.
    - Follows the format (with sample responses from the user):

        My favorite! How many Animal Cupcakes would you like? 5
        Your subtotal for 5 Animal Cupcake is $4.95.

    :param id: the id of the cookie to ask about
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: The quantity the user entered, as an integer.
    """
    # write your code for this function below this line    
    cookie = get_cookie_from_dict(id, cookies)
    name = cookie['title']
    price = cookie['price']
    # cookies_num = input(f'My favorite! How many {name} would you like?')
    while True:
            try:
                cookies_num = int(input(f'My favorite! How many {name} would you like? '))
                if cookies_num > 0:
                    subtotal = cookies_num * price
                    print(f'Your subtotal for {cookies_num} {name} is ${subtotal:.2f}.')
                    return cookies_num
                else:
                    print("Invalid input. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a positive number.")
            
def solicit_order(cookies):
    """
    Takes the complete order from the customer.
    - Asks over-and-over again for the user to enter the id of a cookie they want to order until they enter 'finished', 'done', 'quit', or 'exit'.
    - Validates the id the user enters.
    - For every id the user enters, determines the quantity they want by calling the solicit_quantity function.
    - Places the id and quantity of each cookie the user wants into a dictionary with the format
        {'id': 5, 'quantity': 10}
    - Returns a list of all sub-orders, in the format:
        [
          {'id': 5, 'quantity': 10},
          {'id': 1, 'quantity': 3}
        ]

    :returns: A list of the ids and quantities of each cookies the user wants to order.
    """
    # write your code for this function below this line
    end_words = ['finished', 'done', 'quit', 'exit']
    order = []
    
    while True:
        customer_input = input('Please enter the id of a cookie you would like to order (or type "done" to finish): ')
        if customer_input.lower() in end_words:
            break
        try:
            id = int(customer_input)
            if id < 1 or id > len(cookies):
                print("Invalid cookie id. Please try again.")
            else:
                quantity = solicit_quantity(id, cookies)
                order.append({'id': id, 'quantity': quantity})
        except ValueError:
            print("Invalid input. Please enter a valid cookie id or type 'done' to finish.")
    
    return order

    


def display_order_total(order, cookies):
    """
    Prints a summary of the user's complete order.
    - Includes a breakdown of the title and quantity of each cookie the user ordereed.
    - Includes the total cost of the complete order, formatted to two decimal places.
    - Follows the format:

        Thank you for your order. You have ordered:

        -8 Animal Cupcake
        -1 Basboosa Semolina Cake

        Your total is $11.91.
        Please pay with Bitcoin before picking-up.

        Thank you!
        -The Python Cookie Shop Robot.

    """
    # write your code for this function below this line

    print("\nThank you for your order. You have ordered:\n")
    total_cost = 0.0

    for item in order:
        cookie = get_cookie_from_dict(item['id'], cookies)
        quantity = item['quantity']
        print(f"  - {quantity} {cookie['title']}")
        total_cost += quantity * float(cookie['price'])

    print(f"\nYour total is ${total_cost:.2f}.")
    print("Please pay with Bitcoin before picking-up.")
    print("\nThank you!\n-The Python Cookie Shop Robot.")

def run_shop(cookies):
    """
    Executes the cookie shop program, following requirements in the README.md file.
    - This function definition is given to you.
    - Do not modify it!

    :param cookies: A list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    welcome()
    display_cookies(cookies)
    order = solicit_order(cookies)
    display_order_total(order, cookies)
