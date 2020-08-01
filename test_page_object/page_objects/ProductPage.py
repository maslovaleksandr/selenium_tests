from ..locators import Product
from .DefaultPage import DefaultPage

class ProductPage(DefaultPage):

    def add_to_wish_list(self):
        self.__click(Product.wish_list)

    def add_to_cart(self):
        self.__click(Product.add_to_cart)

    def add_to_compare(self):
        self.click(Product.compare)
