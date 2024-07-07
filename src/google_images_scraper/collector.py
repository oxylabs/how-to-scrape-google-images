"""
    Main module for collecting Google Images data.
"""

import logging

from typing import List

import pandas as pd

from google_images_scraper.scraper import GoogleImagesScraper
from google_images_scraper.models import Image


DEFAULT_OUTPUT_FILE = "images.csv"


class GoogleImagesDataCollector:
    """Data collector class for Google Images"""

    def __init__(
        self,
        output_file: str | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        self._scraper = GoogleImagesScraper()
        self._output_file = output_file if output_file else DEFAULT_OUTPUT_FILE
        self._logger = logger if logger else logging.getLogger(__name__)

    def _save_to_csv(self, images: List[Image]) -> None:
        """Saves given list of images to a CSV file."""
        self._logger.info(f"Writing {len(images)} images to {self._output_file}..")
        image_objects = [image.model_dump() for image in images]
        df = pd.DataFrame(image_objects)
        df.to_csv(self._output_file)

    def get_image_data_for_url(self, url: str) -> None:
        """
        Queries and scrapes data from Google Images for a given image url.

        Args:
            url (str): The URL of the image for which to get Google Images results.
        """
        self._logger.info(f"Getting Google Images data for image url {url}..")
        try:
            images = self._scraper.query_images_for_url(url)
        except Exception:
            self._logger.exception(f"Error when scraping Google Images for url {url}.")
            return

        if not images:
            self._logger.info("No images found.")
            return
        self._save_to_csv(images)
