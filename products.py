def validate_positive_number(input_value):
    if input_value < 0:
        raise ValueError("Input has to be a positive integer.")


def validate_type(input_val, req_type):
    if not isinstance(input_val, req_type):
        raise TypeError


class Product:
    """Single product class that holds name, price and quantity properties"""
    def __init__(self, name, price, quantity):
        """Initiate product class, set name, price, quantity and active"""
        validate_type(name, str)
        validate_type(price, int)
        validate_type(quantity, int)

        validate_positive_number(price)
        validate_positive_number(quantity)

        if name == "":
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
        validate_type(quantity, int)
        validate_positive_number(quantity)
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
        validate_type(quantity, int)
        validate_positive_number(quantity)

        new_quantity = self.quantity - quantity
        if new_quantity < 0:
            raise ValueError(f"Insufficient stock of {self.name}")
        if not self.is_active():
            raise ValueError(f"{self.name} product is inactive")

        self.set_quantity(new_quantity)
        return self.price * quantity


class NonStockedProduct(Product):
    """Single digital product class, child of Product class.
    Has name and price attributes.
    Doesn't track quantity, and quantity is automatically set to 0.
    """
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        pass

    def show(self) -> str:
        """Returns a string that represents the product"""
        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited"

    def buy(self, quantity) -> float:
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        In case of a problem, raises an Exception.
        """
        validate_type(quantity, int)
        validate_positive_number(quantity)

        if not self.is_active():
            raise ValueError(f"{self.name} product is inactive")

        return self.price * quantity


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        if type(maximum) != int:
            raise ValueError("Invalid product input")
        self.max_per_order = maximum

    def show(self) -> str:
        """Returns a string that represents the product"""
        return f"{self.name}, Price: ${self.price}, " \
               f"Limited to {self.max_per_order} per order! "

    def buy(self, quantity) -> float:
        """Buys a given product with max per order amount.
        If quantity is higher than allowed amount, raises an error.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of any other problem, raises an Exception.
        """
        if quantity > self.max_per_order:
            raise ValueError(f"Only {self.max_per_order} "
                             f"allowed per order for this product.")
        return super().buy(quantity)
