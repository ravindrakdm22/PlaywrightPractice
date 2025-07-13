import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser_context(playwright):
    iphone_14 = playwright.devices['iPhone 14']
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(
        record_video_dir="videos/",  # Folder where videos will be saved
        record_video_size={"width": 1280, "height": 720},
        **iphone_14,
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
