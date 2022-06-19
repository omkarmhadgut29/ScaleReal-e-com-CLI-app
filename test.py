from unittest import TestCase
from cart import Cart
from categories import Categories
from products import Product

class TryTesting(TestCase):
    def test_category_returning_list(self):
        categories = Categories()
        categories.list_of_categories()
        self.assertTrue(len(categories.categories) > 0)

    def test_product_returning_list(self):
        product = Product()
        product.list_of_products()
        self.assertTrue(len(product.products) > 0)

    def test_cart_final_price(self):
        cart = Cart()
        cart.view_cart(user_id=1)
        self.assertTrue(cart.cart_item_getting)

    def test_add_to_cart(self):
        cart = Cart()
        product = [1, "Lenevo", 1, "This is lenevo laptop.", 400000]
        cart.add_to_cart(product, 1, user_id=1)
        self.assertTrue(cart.added_to_cart)

