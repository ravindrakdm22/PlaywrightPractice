from playwright.sync_api import Playwright, expect
import pytest


@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"),
                                                pytest.param("visual_user","secret_sauce",
                                                             marks=pytest.mark.skip("skipping for test purpose")),
                                                pytest.param("locked_out_user","secret_sauce1", marks=pytest.mark.xfail)])
def test_first_tc_scratch(playwright: Playwright, username, password) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()

    context.tracing.start(screenshots=True, sources=True, snapshots=True)

    page = context.new_page()
    page.goto("http://www.saucedemo.com")

    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()
    expect(page.locator("//span[text()='Products']")).to_be_visible()
    context.tracing.stop(path="trace_first_tc.zip")
#
#
# with sync_playwright() as playwright:
#     test_first_tc_scratch(playwright)
