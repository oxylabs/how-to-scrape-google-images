"""
    Module for scraping Google Images.
"""

import logging
import time
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from google_images_scraper.conf import google_images_scraper_settings
from google_images_scraper.models import Image


logging.getLogger("WDM").setLevel(logging.ERROR)


class ConsentFormAcceptError(BaseException):
    message = "Unable to accept Google consent form."


class DriverInitializationError(BaseException):
    message = "Unable to initialize Chrome webdriver for scraping."


class DriverGetImageDataError(BaseException):
    message = "Unable to get Google Image data with Chrome webdriver."


class GoogleImagesScraper:
    """Class for scraping Google Images"""

    def __init__(self, logger: logging.Logger | None = None) -> None:
        self._logger = logger if logger else logging.getLogger(__name__)
        self._consent_button_xpath = "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span"

    def _init_chrome_driver(self) -> webdriver.Chrome:
        """Initializes Chrome webdriver"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=chrome_options)

    def _click_consent_button(self, driver: webdriver.Chrome) -> None:
        """Clicks google consent form with selenium Chrome webdriver"""
        self._logger.info("Accepting consent form..")
        try:
            driver.get(google_images_scraper_settings.lens_url)
            consent_button = driver.find_element(
                By.XPATH,
                self._consent_button_xpath,
            )
            consent_button.click()
        except Exception as e:
            raise ConsentFormAcceptError from e

        time.sleep(2)

    def _get_data_from_image_div(self, div: webdriver.Chrome) -> Image:
        """Retrieves image data from a div element and returns it as an Image object."""
        a_element = div.find_element(By.TAG_NAME, "a")
        title = a_element.get_attribute("aria-label")
        source_url = a_element.get_attribute("href")
        img_element = div.find_element(By.TAG_NAME, "img")
        image_url = img_element.get_attribute("data-src") or img_element.get_attribute(
            "src"
        )
        return Image(title=title, url=image_url, source_url=source_url)

    def _get_images_from_page(self, url: str, driver: webdriver.Chrome) -> List[Image]:
        """Retrieves image data from a Google Images search page."""
        self._logger.info("Scraping Google Images page..")
        driver.get(google_images_scraper_settings.get_upload_url_for_image(url))
        image_divs = driver.find_elements(By.CLASS_NAME, "G19kAf")
        return [self._get_data_from_image_div(div) for div in image_divs]

    def query_images_for_url(self, url: str) -> List[Image]:
        """
        Retrieves a list of images queried in Google Images for a given image URL.

        Returns:
            List[Image]: A list of Image objects.
        Raises:
            ConsentFormAcceptError: If the Google consent form cannot be accepted.
            DriverInitializationError: If the Chrome webdriver cannot be initialized.
            DriverGetImageDataError: If the image data cannot be scraped from the Google Images site.
        """
        self._logger.info(f"Retrieving images for {url}..")

        try:
            driver = self._init_chrome_driver()
        except Exception as e:
            raise DriverInitializationError from e

        try:
            self._click_consent_button(driver)
        except Exception as e:
            driver.close()
            raise e

        try:
            return self._get_images_from_page(url, driver)
        except Exception as e:
            raise DriverGetImageDataError from e
        finally:
            driver.close()
