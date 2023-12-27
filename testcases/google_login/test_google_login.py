# -*- coding: utf-8 -*-
import allure
import pytest
from utils import get_json_data


@allure.severity("normal")
@pytest.mark.normal
@pytest.mark.parametrize("email", ["null"])
def test_google_login_error_account_using_parameter(google_login_page, email):
    google_login_page.enter_email(email=email)
    assert google_login_page.check_email_not_found_prompt()


@allure.severity("normal")
@pytest.mark.normal
def test_google_login_error_account_using_data(google_login_page):
    data = get_json_data(json_name="account")
    google_login_page.enter_email(email=data["email"])
    assert google_login_page.check_email_not_found_prompt()
