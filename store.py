from typing import List, Dict


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
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List:
        """Returns all products in the store that are active."""
        return [product for product in self.products_list if product.active]

    def generate_order_dict(self, shopping_list: List[tuple]) -> Dict:
        """Generate and return a final shopping dictionary from shopping list,
        with products as keys, and final order quantity for each product
        as values."""
        shopping_dict = {}
        for product, quantity in shopping_list:
            if product not in shopping_dict:
                shopping_dict[product] = 0
            shopping_dict[product] += quantity
        return shopping_dict

    def order(self, shopping_list: List[tuple]) -> float:
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        In case of a problem, prints the error.
        """
        total_cost = 0
        shopping_dict = self.generate_order_dict(shopping_list)
        for product, quantity in shopping_dict.items():
            try:
                buy_price = product.buy(quantity)
                print(f"{product.name} was successfully purchased.")
            except ValueError as error:
                print(f"Error while processing the order! {error}")
                break
            total_cost += buy_price
        return total_cost
