import pytest
from products import Product, NonStockedProduct, LimitedProduct


# Using the library pytest, create the following tests (Remember - each test should have it’s own function):
# Test that creating a normal product works.
def test_product_init_creation():
    product_instance = Product(name="Test product", price=150, quantity=50)
    assert isinstance(product_instance, Product)
    assert product_instance.get_quantity() == 50
    assert product_instance.price == 150
    assert product_instance.name == "Test product"
    assert product_instance.active is True


# Test that creating a product with invalid details (empty name, negative price) invokes an exception.
def test_product_init_empty_name():
    with pytest.raises(ValueError):
        Product(name="", price=150, quantity=50)


def test_product_init_negative_price():
    with pytest.raises(ValueError):
        Product(name="Test product", price=-150, quantity=50)


def test_product_init_negative_quantity():
    with pytest.raises(ValueError):
        Product(name="Test product", price=150, quantity=-50)


# Test that when a product reaches 0 quantity, it becomes inactive.
def test_product_quantity_0():
    product_instance = Product(name="Test product", price=150, quantity=50)
    product_instance.set_quantity(0)
    assert product_instance.active is False


# Test that product purchase modifies the quantity and returns the right output.
def test_product_buy_method():
    product_instance = Product(name="Test product", price=150, quantity=50)
    product_instance.buy(5)
    assert product_instance.quantity == 45


# Test that buying a larger quantity than exists invokes exception.
def test_product_buy_too_much():
    with pytest.raises(ValueError):
        product_instance = Product(name="Test product", price=150, quantity=50)
        product_instance.buy(51)


# Test NonStockedProduct - Buy any amount
def test_non_stocked_buy_many():
    non_stock_inst = NonStockedProduct(name="Digital product", price=100)
    assert non_stock_inst.buy(50000) == 5000000


# Check quantity always stays 0
def test_non_stocked_quantity_always_0():
    non_stock_inst = NonStockedProduct(name="Digital product", price=100)
    assert non_stock_inst.quantity == 0
    non_stock_inst.buy(50000)
    assert non_stock_inst.quantity == 0


# LimitedProduct - Check lower than max amount
def test_limited_normal_amount():
    limited_inst = LimitedProduct(name="Shipping", price=50, quantity=100,
                                  maximum=2)
    assert limited_inst.buy(2) == 100


# Check over max amount
def test_limited_over_allowed():
    with pytest.raises(ValueError):
        limited_inst = LimitedProduct(name="Shipping", price=50, quantity=100,
                                      maximum=2)
        limited_inst.buy(3)


# Check max_per_order input raises error if wrong type
def test_limited_wrong_type_max_per_order():
    with pytest.raises(ValueError):
        LimitedProduct(name="Shipping", price=50, quantity=100,
                       maximum="Unlimited")


pytest.main()
