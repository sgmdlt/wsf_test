import pytest
from tests.utils import get_fixture
from scraper.html import get_children, make_full_url

PARENT_URL = 'https://minobrnauki.gov.ru/about/deps/'
CHILD_URLS = [
    'https://minobrnauki.gov.ru/about/deps/ad/',
    'https://minobrnauki.gov.ru/about/deps/daninpr/',
    'https://minobrnauki.gov.ru/about/deps/dbi/',
    ]


@pytest.fixture
def page():
    fixture = get_fixture('parent_page.html') 
    return open(fixture, 'r')


def test_get_children(page):
    urls = get_children(page)
    full_urls = [make_full_url(PARENT_URL, url) for url in urls]
    assert full_urls == CHILD_URLS