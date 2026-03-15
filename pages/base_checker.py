from pages.base_page import BasePage
from assertpy import assert_that
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError  # ← вот так правильно


class BaseChecker(BasePage):

    def check_presence_of_element(self, locator: str, timeout: 5000) -> bool:
        try:
            self.page.wait_for_selector(locator, timeout=timeout)
            return True
        except PlaywrightTimeoutError as e:
            return False