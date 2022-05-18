install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 scraper/

check: test lint

run:
	poetry run scraper