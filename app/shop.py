from app.customer import Customer
from datetime import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def products_cost(self, customer: Customer) -> float:
        product_cart = customer.product_cart
        product_cost = 0
        for product, qty in product_cart.items():
            product_cost += qty * self.products.get(product)
        return product_cost

    def print_check(self, customer: Customer) -> None:
        current_datatime = datetime(2021, 1, 4, 12, 33, 41)
        current_datatime = current_datatime.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_datatime}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        milk = customer.product_cart.get("milk")
        print(f"{milk} "
              f"milks for "
              f"{milk * self.products.get('milk')}"
              f" dollars")
        bread = customer.product_cart.get("bread")
        print(f"{bread} "
              f"breads for "
              f"{round(bread * self.products.get('bread'))}"
              f" dollars")
        butter = customer.product_cart.get("butter")
        print(f"{butter}"
              f" butters for "
              f"{butter * self.products.get('butter')}"
              f" dollars")
        print(f"Total cost is {self.products_cost(customer)} dollars")
        print("See you again!\n")
