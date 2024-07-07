"""
    Pydantic models for Google Images scraper.
"""

from pydantic import BaseModel


class Image(BaseModel):
    title: str
    url: str
    source_url: str
