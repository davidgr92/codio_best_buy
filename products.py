class Product:
    """Single product class that holds name, price and quantity properties"""
    def __init__(self, name, price, quantity):
        """Initiate product class, set name, price, quantity and active"""
        if name == "" or price < 0 or quantity < 0:
            raise ValueError("Invalid product input")
        self.name: str = name
        self.price: float = price
        self.quantity: int = quantity
        self.active: bool = True

    def get_quantity(self) -> float:
        """Getter function for quantity. Returns the quantity (float)."""
        return self.quantity

    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0,
        deactivates the product.
        """
        self.quantity = quantity
        if self.get_quantity() == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Getter function for active. Returns True if the product is active,
        otherwise False.
        """
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self) -> str:
        """Returns a string that represents the product"""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem, raises an Exception.
        """
        new_quantity = self.quantity - quantity
        if new_quantity < 0:
            raise ValueError(f"Insufficient stock of {self.name}")
        if not self.is_active():
            raise ValueError(f"{self.name} product is inactive")

        self.set_quantity(new_quantity)
        return self.price * quantity


def main():
    """Main test function for module"""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50) == 12500)
    print(mac.buy(100) == 145000)
    print(mac.is_active() is False)

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())

    print(mac.buy(1))


if __name__ == '__main__':
    main()
