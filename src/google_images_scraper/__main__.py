"""
    Main module for google_images_scraper.
"""

import logging

import click

from google_images_scraper.collector import GoogleImagesDataCollector


logging.basicConfig(level=logging.INFO)


@click.command()
@click.option(
    "--url",
    help="The url for which to return Google Images results for.",
    required=True,
)
def scrape_google_images(url: str) -> None:
    collector = GoogleImagesDataCollector()
    collector.get_image_data_for_url(url)


if __name__ == "__main__":
    scrape_google_images()
