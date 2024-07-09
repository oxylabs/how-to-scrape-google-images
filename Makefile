# Makefile for running the Google Images scraper


.PHONY: install
install:
	pip install poetry==1.8.2
	poetry install


.PHONY: scrape
scrape:
	@if [ -z "$(URL)" ]; then \
		echo 'Error: A URL of an image to query is required. Use make scrape URL="<image_url>"'; \
		exit 1; \
	else \
		poetry run python -m google_images_scraper --url="$(URL)"; \
	fi
