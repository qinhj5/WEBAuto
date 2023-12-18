# -*- coding: utf-8 -*-
import pytest
from utils import get_json_data


@pytest.mark.parametrize("email", ["null"])
def test_google_login_error_account_using_parameter(google_login_page, email):
    google_login_page.enter_email(email=email)
    assert google_login_page.check_email_not_found_prompt()


def test_google_login_error_account_using_data(google_login_page):
    data = get_json_data(json_name="account")
    google_login_page.enter_email(email=data["email"])
    assert google_login_page.check_email_not_found_prompt()
