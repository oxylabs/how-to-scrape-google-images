"""
    Config module for google_images_scraper.
"""

from urllib.parse import urljoin

from pydantic_settings import BaseSettings


class GoogleImagesScraperSettings(BaseSettings):
    """Settings class for Google Images Scraper"""

    lens_url: str = "https://lens.google.com/"

    def get_upload_url_for_image(self, url: str) -> str:
        return urljoin(self.lens_url, f"uploadbyurl?url={url}")


google_images_scraper_settings = GoogleImagesScraperSettings()
