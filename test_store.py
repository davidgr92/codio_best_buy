import pytest
from store import Store
from products import Product, LimitedProduct, NonStockedProduct


# Test store creation
def test_store_creation():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)]

    best_buy = Store(product_list)
    assert len(best_buy.products_list) == 5


# Test add product method - adds a product to store property
def test_store_add_product():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)]

    best_buy = Store(product_list)
    best_buy.add_product(NonStockedProduct("Test Product", 150))
    assert len(best_buy.products_list) == 6


# Test remove product method - removes a product from store property
def test_store_remove_product():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)]

    best_buy = Store(product_list)
    best_buy.remove_product(product_list[0])
    assert len(best_buy.products_list) == 4


# Test get total quantity method
def test_store_get_total_quantity():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)]

    best_buy = Store(product_list)
    assert best_buy.get_total_quantity() == 1100


# Test get all products
def test_store_get_all_products():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)]

    best_buy = Store(product_list)
    assert best_buy.get_all_products() == product_list


# Test order method - normal
def test_store_order():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)]

    best_buy = Store(product_list)
    shopping_list = [(product_list[1], 50),
                     (product_list[3], 50),
                     (product_list[-1], 1)]
    assert best_buy.order(shopping_list) == 18760


# Test order method - handles errors
def test_store_order_errors():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)]

    best_buy = Store(product_list)
    shopping_list = [(product_list[1], 50),
                     (product_list[3], 50),
                     (product_list[-1], 2)]
    assert best_buy.order(shopping_list) == 18750


pytest.main()
