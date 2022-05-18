install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 scraper/

check: test lint

run:
	poetry run scraper

test-coverage:
	poetry run pytest --cov=scraper --cov-report xml