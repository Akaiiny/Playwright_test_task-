import allure
from pages.base_page import BasePage


class PlaywrightHomePage(BasePage):

    @allure.step("Проверяем заголовок страницы на '{expected_text}'")
    def verify_header_correctness(self, header_locator: str) ->  None:
        header = self.find_element(header_locator)
