from playwright.sync_api import Playwright, expect
import pytest


@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"),
                                                pytest.param("visual_user","secret_sauce",
                                                             marks=pytest.mark.skip("skipping for test purpose")),
                                                pytest.param("locked_out_user","secret_sauce1", marks=pytest.mark.xfail)])
def test_first_tc_scratch(page, username, password) -> None:
    page.goto("http://www.saucedemo.com")

    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()
    expect(page.locator("//span[text()='Products']")).to_be_visible()

#
#
# with sync_playwright() as playwright:
#     test_first_tc_scratch(playwright)
