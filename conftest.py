import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser_context(playwright):
    iphone_15 = playwright.devices['iPhone 15']
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(
        **iphone_15,
    )
    # browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    # context = browser.new_context()
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )
    yield context
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()

@pytest.fixture(scope="function")
def page(browser_context):
    return browser_context.new_page()
