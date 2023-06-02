import products
import store
import promotions


def list_all_products_in_store(store_class):
    """Print all products in store with their name, price and quantity,
    Returns dictionary with number key and product object as value.
    """
    print("------")
    products_dict = {}
    active_products = store_class.get_all_products()
    if active_products:
        for i, product in enumerate(active_products, 1):
            print(f"{i}. {product.show()}")
            products_dict[i] = product
    else:
        print("No more products in store. ")
    print("------")
    return products_dict


def show_total_amount_in_store(store_class):
    """Calculates and prints total product quantity in store"""
    total_quantity = store_class.get_total_quantity()
    print(f"Total of {total_quantity} items in store")


def make_an_order(store_class):
    """Makes an order, takes user inputs and calls the store class
    order method with the user shopping list.
    Buys each item in shopping list and returns final total order price.
    """
    products_dict = list_all_products_in_store(store_class)
    if not products_dict:
        print("Sorry, we have no products in stock. Action unavailable.")
        return
    order_list = []
    print("When you want to finish order, enter empty text.")
    while True:
        try:
            order_item = get_order_item(products_dict)
        except ValueError as error:
            print(f"Error while taking order! {error}\n")
            continue
        if order_item[0] == "" or order_item[1] == "":
            break
        order_list.append(order_item)
        print("Product added to shopping list!\n")

    if order_list:
        total_cost = store_class.order(order_list)
        print(f"Order made! Total payment: ${total_cost}")
    else:
        print("Order was canceled.")


def get_order_item(products_dict) -> tuple:
    """Get order item from user, validate it,
    and raise exception if there is a problem
    """
    prod_num = input("Which product # do you want? ")
    if prod_num == "":
        return "", ""
    if prod_num.isnumeric() and int(prod_num) in products_dict:
        quantity = input("What amount do you want? ")
        if quantity == "":
            return "", ""
        if quantity.isnumeric():
            return products_dict[int(prod_num)], int(quantity)
        raise ValueError("Wrong quantity input")
    raise ValueError("Wrong product input")


class BreakException(BaseException):
    """Break exception to break out of a loop from inside a function"""


def quit_program(store_class):
    """Quits the main loop"""
    raise BreakException


def print_functions_list(func_list):
    """Print a list of available actions and their corresponding num key"""
    print("\n   Store Menu\n   ----------")
    for key, action in func_list.items():
        print(f"{key}. {action.__name__.replace('_', ' ').capitalize()}")
    print()


def get_action_num(func_list):
    """Get valid action num key from the user"""
    print_functions_list(func_list)
    while True:
        action = input("Please choose an action number: ")
        if action.isnumeric() and int(action) in func_list:
            return int(action)
        print("Wrong input, try again")


def main():
    """Initiate main function"""
    functions_list = {
        1: list_all_products_in_store,
        2: show_total_amount_in_store,
        3: make_an_order,
        4: quit_program
    }

    product_list = [products.Product("MacBook Air M2", price=1450,
                                     quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250,
                                     quantity=500),
                    products.Product("Google Pixel 7", price=500,
                                     quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10,
                                            quantity=250, maximum=1)
                    ]

    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)

    try:
        while True:
            action = get_action_num(functions_list)
            functions_list[action](best_buy)
    except BreakException:
        pass


if __name__ == '__main__':
    main()
