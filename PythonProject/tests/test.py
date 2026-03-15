import allure
from playwright.sync_api import expect
from pages.playwright_home_page import PlaywrightHomePage
from pages.page_locators import PlaywrightPageLocators
from time import sleep
@allure.title("Проверка заголовка главной страницы Playwright")
@allure.description_html(
    "Открываем <b>https://playwright.dev</b> и проверяем title + основной заголовок"
)
@allure.tag("smoke", "ui", "playwright")
@allure.severity(allure.severity_level.NORMAL)
def test_main_page_title(page):
    home = PlaywrightHomePage(page)
    home.open()
    header = home.find_element(PlaywrightPageLocators.HEADER)
    expect(header).to_have_text(
        "Playwright enables reliable end-to-end testing for modern web apps."
    )