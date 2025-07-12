from playwright.sync_api import sync_playwright, Playwright, expect


def test_first_tc_scratch(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()

    context.tracing.start(screenshots=True, sources=True, snapshots=True)

    page = context.new_page()
    page.goto("http://www.saucedemo.com")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page.locator("//span[text()='Products']")).to_be_visible()
    context.tracing.stop(path="trace_first_tc.zip")


with sync_playwright() as playwright:
    test_first_tc_scratch(playwright)
