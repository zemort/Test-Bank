from src.main.ui.pages.login_page import LoginPage
from src.main.ui.steps.catalog_steps import CatalogSteps
from src.main.ui.steps.login_steps import LoginSteps

def test_auth(page):
    steps = LoginSteps(page)
    steps.open_login_page().login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_login_locked_out_user(page):
    steps = LoginSteps(page)
    steps.open_login_page().login("locked_out_user", "secret_sauce")
    assert page.url == LoginPage.URL

    error_text = steps.get_error_text()
    assert "locked out" in error_text

def test_logout(page):
    steps = LoginSteps(page)
    catalog = CatalogSteps(page)
    steps.open_login_page().login("standard_user", "secret_sauce")
    assert catalog.get_cart_count() > 0

    catalog.logout()

    assert page.url == steps.LOGIN_URL

def test_logout_visual_user(page):
    steps = LoginSteps(page)
    catalog = CatalogSteps(page)

    steps.login_page.login("visual_user", "secret_sauce")
    assert catalog.get_cart_count() > 0

    catalog.logout()
    assert page.url == steps.LOGIN_URL