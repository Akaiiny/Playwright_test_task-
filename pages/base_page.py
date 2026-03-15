from playwright.sync_api import Page, Locator, expect, ElementHandle


class BasePage:
    """Базовый класс для всех Page Objects. Содержит общие методы."""

    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://playwright.dev/"

    def open(self):
        self.page.goto(self.base_url, wait_until="load")

    def find_element(self, selector: str) -> Locator:
        element = self.page.locator(selector)
        if element is None:
            raise ValueError(f"Элемент по селектору '{selector}' не найден")
        return element