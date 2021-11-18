"""
Krótka wiadomość odnośnie kodu, idąc dalej w refactoring zauważyłem, że zaczynam robić cały system obsługi kasy,
gdzie co chwile pojawiały się pomysły, żeby zdefiniować różne warunki, gdzie je trzymać, kolejne zniżki, rodzaje produktów itd.,
w pewnym momencie postanowiłem ukrócić ten proces i uprościłem kilka rzeczy gdzie skrypt docelowo ma porównać 2 promocje.
"""

from enum import Enum
from dataclasses import dataclass
import typing as t


class Discount(Enum):
    whole_basket: float = 0.99
    beef: float = 0.9


@dataclass(frozen=True)
class Product:
    name: str
    price: float
    quantity: int

    @property
    def total_value(self) -> float:
        return self.price * self.quantity

    def after_promotion(self, discount: Discount) -> float:
        """Return value of product after discount."""
        return self.total_value * discount.value


class Basket:
    def __init__(self):
        self.basket: t.List[Product] = []

    def add(self, product: Product) -> t.NoReturn:
        """Add products to basket."""
        self.basket.append(product)

    def _apply_discount(self, discount_enum: Discount) -> float:
        """Return basket value after implemented discount."""
        CONDITION = 700  # as an example I'm giving fixed value instead of building condition mechanism
        return sum([product.after_promotion(discount_enum) if product.price > CONDITION else product.total_value
                    for product in self.basket])

    def compare_promotion(self) -> t.NoReturn:
        """Compare what is better for a customer, full 1% basket discount or chosen product discount."""
        one_percent_value = sum(
            [product.total_value for product in self.basket]) * Discount.whole_basket.value
        ten_percent_value = self._apply_discount(Discount.beef)
        return max(one_percent_value, ten_percent_value)

    @property
    def total_value(self):
        """Always checks value promotions in this case"""
        return self.compare_promotion()

    def remove(self, product_name: str) -> t.NoReturn:
        for product in self.basket:
            if product.name == product_name:
                self.basket.remove(product)


basket = Basket()
items = [(('beef', 1000), 0.75),
         (('spam', 10), 1),
         (('egg', 6), 7 * 8),
         (('ham', 10), 1),
         (('colored pencils in a box', 98), 1)]

for item in items:
    basket.add(Product(item[0][0], item[0][1], item[1]))

# Value without discount
assert sum(product.total_value for product in basket.basket) == 1204.0
# Better discount
assert basket.total_value == 1191.96

# After removing beef
basket.remove('beef')
assert sum(product.total_value for product in basket.basket) == 454.0