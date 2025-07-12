# import re
# from playwright.sync_api import Playwright, sync_playwright, expect
#
#
# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.saucedemo.com/")
#     page.locator("[data-test=\"login-credentials\"]").click()
#     page.locator("[data-test=\"username\"]").click()
#     page.locator("[data-test=\"username\"]").fill("standard_user")
#     page.locator("[data-test=\"username\"]").press("Tab")
#     page.locator("[data-test=\"password\"]").fill("secret_sauce")
#     page.locator("[data-test=\"login-button\"]").click()
#     page.locator("[data-test=\"secondary-header\"]").click(button="right")
#     page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
#     page.locator("[data-test=\"shopping-cart-link\"]").click()
#     page.locator("[data-test=\"checkout\"]").click()
#     page.locator("[data-test=\"firstName\"]").click()
#     page.locator("[data-test=\"firstName\"]").fill("r")
#     page.locator("[data-test=\"firstName\"]").press("Tab")
#     page.locator("[data-test=\"lastName\"]").fill("k")
#     page.locator("[data-test=\"lastName\"]").press("Tab")
#     page.locator("[data-test=\"postalCode\"]").fill("123456")
#     page.locator("[data-test=\"continue\"]").click()
#     page.locator("[data-test=\"finish\"]").click()
#     page.locator("[data-test=\"back-to-products\"]").click()
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)
