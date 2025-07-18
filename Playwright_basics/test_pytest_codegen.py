import re
from playwright.sync_api import expect

def test_example(page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"primary-header\"] div").filter(has_text="Swag Labs").first).to_be_visible()
    expect(page.get_by_text("Swag Labs")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    expect(page.locator("[data-test=\"primary-header\"]")).to_contain_text("Swag Labs")
    page.locator("[data-test=\"item-4-title-link\"]").click()
    expect(page.locator("[data-test=\"back-to-products\"]")).to_contain_text("Back to products")
    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Backpack")
    expect(page.locator("[data-test=\"inventory-item-price\"]")).to_contain_text("$29.99")
    page.locator("[data-test=\"add-to-cart\"]").click()
    page.locator("[data-test=\"back-to-products\"]").click()
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
    expect(page.locator("[data-test=\"shopping-cart-badge\"]")).to_contain_text("1")
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"checkout\"]")).to_be_visible()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_be_visible()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_contain_text("Remove")
    expect(page.locator("[data-test=\"checkout\"]")).to_contain_text("Checkout")
    page.locator("[data-test=\"checkout\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Your Information")
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("r")
    page.locator("[data-test=\"firstName\"]").press("Tab")
    page.locator("[data-test=\"lastName\"]").fill("k")
    page.locator("[data-test=\"lastName\"]").press("Tab")
    page.locator("[data-test=\"postalCode\"]").fill("123456")
    page.locator("[data-test=\"continue\"]").click()
    expect(page.locator("[data-test=\"payment-info-label\"]")).to_be_visible()
    page.locator("[data-test=\"shipping-info-label\"]").click()
    page.locator("[data-test=\"shipping-info-label\"]").click()
    expect(page.locator("[data-test=\"total-info-label\"]")).to_be_visible()
    expect(page.locator("[data-test=\"total-label\"]")).to_contain_text("Total: $32.39")
    expect(page.locator("[data-test=\"tax-label\"]")).to_contain_text("Tax: $2.40")
    expect(page.locator("[data-test=\"subtotal-label\"]")).to_contain_text("Item total: $29.99")
    page.locator("[data-test=\"finish\"]").click()
    expect(page.locator("[data-test=\"pony-express\"]")).to_be_visible()
    expect(page.locator("[data-test=\"complete-header\"]")).to_contain_text("Thank you for your order!")
    expect(page.locator("[data-test=\"complete-text\"]")).to_contain_text("Your order has been dispatched, and will arrive just as fast as the pony can get there!")
    expect(page.locator("[data-test=\"back-to-products\"]")).to_be_visible()
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()
    expect(page.locator("[data-test=\"login-button\"]")).to_be_visible()