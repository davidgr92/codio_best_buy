from typing import List
from products import Product


class Store:
    """Store class that holds current stock of available product items"""
    def __init__(self, products_list: list):
        """Initiate class sets products list in the store class"""
        self.products_list = products_list

    def add_product(self, product):
        """Adds a product to store products_list"""
        self.products_list.append(product)

    def remove_product(self, product):
        """Removes a product from store products_list"""
        self.products_list.remove(product)

    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        total_quantity = 0
        for product in self.products_list:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self) -> List[Product]:
        """Returns all products in the store that are active."""
        return [product for product in self.products_list if product.active]

    def order(self, shopping_list: List[tuple]) -> float:
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        In case of a problem, prints the error.
        """
        total_cost = 0
        for product, quantity in shopping_list:
            try:
                buy_price = product.buy(quantity)
                print(f"{product.name} was successfully purchased.")
            except ValueError as error:
                print(f"Error while processing the order! {error}")
                break
            total_cost += buy_price
        return total_cost


def main():
    """Main test function for module"""
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()
    store.add_product(Product("Bla bla bla", price=-100, quantity=10))
    print(store.get_total_quantity() == 850)
    print(store.order([(products[0], 1), (products[1], 2)]) == 1950)


if __name__ == '__main__':
    main()
