import pytest
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount
from products import Product


def test_second_half_off_even():
    promotion = SecondHalfPrice("Test!")
    product = Product("Test Product", price=10, quantity=2000)
    assert promotion.apply_promotion(product, 10) == 75


def test_second_half_off_odd():
    promotion = SecondHalfPrice("Test Again!")
    product = Product("Test Product", price=10, quantity=2000)
    assert promotion.apply_promotion(product, 13) == 100


def test_third_one_free_divides_in_3():
    promotion = ThirdOneFree("One More!")
    product = Product("Test Product", price=10, quantity=2000)
    assert promotion.apply_promotion(product, 12) == 80


def test_third_one_free_not_divides_in_3():
    promotion = ThirdOneFree("One More!")
    product = Product("Test Product", price=10, quantity=2000)
    assert promotion.apply_promotion(product, 14) == 100


def test_percent_discount_35():
    promotion = PercentDiscount("Last One", 35)
    product = Product("Test Product", price=10, quantity=2000)
    assert promotion.apply_promotion(product, 14) == 91


def test_percent_discount_20():
    promotion = PercentDiscount("Last One", 20)
    product = Product("Test Product", price=10, quantity=2000)
    assert promotion.apply_promotion(product, 14) == 112


pytest.main()
