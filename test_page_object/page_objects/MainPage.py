from ..locators import Main
from .DefaultPage import DefaultPage


class MainPage(DefaultPage):

    def click_featured_products(self, number):
        index = number - 1
        self.__click(Main.featured.elements, index=index)
    

    def get_featured_products_text(self, number):
        index = number-1
        self._get_text(Main.featured.names, index=index)

