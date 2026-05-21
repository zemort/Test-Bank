import allure
from src.main.ui.pages.basket_page import BasketPage
from playwright.sync_api import Page

class BasketSteps:
    def __init__(self, page: Page):
        self.page = page
        self.basket = BasketPage(page)

    @allure.step("Открытие корзины")
    def open_cart(self):
        self.basket.open_cart()
        return self

    @allure.step("Переход в checkout")
    def checkout(self):
        self.checkout()
        return self

    @allure.step("Удаление товар {product_name}")
    def remove_item(self, product_name: str):
        self.remove_item(product_name)
        return self

    @allure.step("Проверяем товар в корзине {product_name}")
    def expect_item_in_cart(self, product_name: str):
        self.expect_item_in_cart(product_name)
        return self

    @allure.step("Проверяем что товара {product_name} нет в корзине")
    def expect_item_not_in_cart(self, product_name: str):
        self.expect_item_not_in_cart(product_name)
        return self

    @allure.step("Получаем список названий товаров в корзине")
    def get_item_names(self) -> list[str]:
        return self.basket.get_item_names()

    @allure.step("Получаем общую сумму товаров в корзине")
    def get_item_total_price(self) -> float:
        return self.basket.get_item_total_price()