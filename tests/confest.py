import os.path
import pytest
from playwright.sync_api import Playwright, sync_playwright
from data.browser_data import BrowsersData


@pytest.fixture(scope="function")
def playwright() -> Playwright:
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="function", params=BrowsersData.browsers_list)
def browser(request, playwright: Playwright):
    if request.param == "firefox":
        browser = playwright.firefox.launch(headless=True)
    elif request.param == "chrome":
        browser = playwright.chromium.launch(headless=True)
    else:
        raise ValueError(f"Unsupported browser: {request.param}")
    permissions = ["geolocation"]
    context = browser.new_context(permissions=permissions)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.wait_for_load_state(state="domcontentloaded")
    yield page
    traces_dr = os.path.join(os.getcwd(), "traces")
    os.makedirs(traces_dr, exist_ok=True)

    trace_path = os.path.join(traces_dr, f"{request.node.name}_trace.zip")
    context.tracing.stop(path=trace_path)
    page.close()
    context.close()
    browser.close()