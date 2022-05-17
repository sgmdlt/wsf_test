import pytest
from scraper.html import get_images
from tests.utils import get_fixture


IMAGES = [
    ('Казакова Татьяна Вячеславовна', '/upload/iblock/e13/e13f1c6a4d7d81d82f710f455ef4d5e7.jpg'),
    ('Копылова Александра Олеговна','/upload/iblock/746/7462437d69c0b291f65964dd9330d82e.jpg'),
    ('Петровичева Светлана Владимировна','/upload/iblock/cdb/cdb477fefd27636524213f472c71b7a9.jpg'),
    (' ','/upload/iblock/39f/2gvxocrus56bzq9k4egjnkrvm2y04d45.png'),
]


@pytest.fixture
def page():
    fixture = get_fixture('page_with_images.html') 
    return open(fixture, 'r')

def test_get_images(page):
    assert get_images(page) == IMAGES