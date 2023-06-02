from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract promotion class template"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class SecondHalfPrice(Promotion):
    """Second item half price promotion"""
    def apply_promotion(self, product, quantity) -> float:
        if quantity % 2 == 1:
            return 0.75 * (quantity - 1) * product.price + product.price
        return 0.75 * quantity * product.price


class ThirdOneFree(Promotion):
    """Third item for free promotion"""
    def apply_promotion(self, product, quantity) -> float:
        if quantity % 3 == 0:
            return 2 * quantity * product.price / 3
        return product.price * (2 * (quantity // 3) + quantity % 3)


class PercentDiscount(Promotion):
    """Percentage discount promotion"""
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        return quantity * product.price * (100 - self.percent) / 100




