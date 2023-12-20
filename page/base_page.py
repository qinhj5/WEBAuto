# -*- coding: utf-8 -*-
import os
import allure
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from utils import set_allure_and_console_output, logger, get_current_datetime


class BasePage:

    def __init__(self, url: str) -> None:
        """
        Initialize an instance of the BasePage class.

        Args:
            url (str): The URL of the web page to be loaded.

        Returns:
            None
        """
        self.options = Options()
        self.options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(url)

    def find_element(self, *loc: tuple) -> WebElement:
        """
        Find a single element on the web page.

        Args:
            *loc (tuple): Variable length argument representing the locator of the element.

        Returns:
            WebElement: The found element.
        """
        set_allure_and_console_output("find element", f"{loc}")
        element = None
        try:
            element = self.driver.find_element(*loc)
        except Exception as e:
            logger.error(e)
        finally:
            return element

    def find_elements(self, *loc: tuple) -> List[WebElement]:
        """
        Find multiple elements on the web page.

        Args:
            *loc (tuple): Variable length argument representing the locator of the elements.

        Returns:
            List[WebElement]: The found elements.
        """
        set_allure_and_console_output("find elements", f"{loc}")
        elements = None
        try:
            elements = self.driver.find_elements(*loc)
        except Exception as e:
            logger.error(e)
        finally:
            return elements

    def save_screenshot(self) -> None:
        """
        Save a screenshot of the current page.

        Returns:
            None
        """
        page_dir = os.path.dirname(os.path.abspath(__file__))
        screenshot_dir = os.path.abspath(os.path.join(page_dir, "../screenshot"))
        screenshot_path = os.path.abspath(os.path.join(screenshot_dir, f"screenshot {get_current_datetime()}.png"))
        self.driver.get_screenshot_as_file(screenshot_path)
        allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG)
