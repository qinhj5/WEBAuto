# -*- coding: utf-8 -*-
from utils import logger
from page.base_page import BasePage


class GoogleLoginPage(BasePage):
    login_entrance_button = ("xpath", """//span[@class="entrance"]""")
    email_input = ("xpath", """//input[@id="identifierId"]""")
    next_button = ("xpath", """//*[@id="identifierNext"]/div/button/span""")
    email_not_found_prompt = ("xpath", """//div[@class="prompt"]""")

    def enter_email(self, email: str) -> None:
        """
        Enter email action.

        Args:
            email (str): Email.

        Returns:
            None
        """
        logger.info("Click: Login entrance")
        self.find_element(*self.login_entrance_button).click()

        logger.info("Input email: {}".format(email))
        self.find_element(*self.email_input).send_keys(email)

        logger.info("Click: Next")
        self.find_element(*self.next_button).click()

    def check_email_not_found_prompt(self) -> bool:
        """
        Check if the email prompt is found.

        Returns:
            bool: True if found, False otherwise.
        """
        element = self.find_element(*self.email_not_found_prompt)
        if element is None:
            logger.info("Email prompt not found")
            return False
        else:
            logger.info("Found email prompt")
            return True
