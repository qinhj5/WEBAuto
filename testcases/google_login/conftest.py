# -*- coding: utf-8 -*-
import pytest
from config import Global
from page.google_login.google_login_page import GoogleLoginPage


@pytest.fixture(scope="function")
def google_login_page():
    google_login_page = GoogleLoginPage(url=Global.constants.GOOGLE_LOGIN_URL)
    yield google_login_page
    google_login_page.save_screenshot()
    google_login_page.driver.quit()
