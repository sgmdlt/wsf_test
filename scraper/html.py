import unicodedata
from urllib.parse import urljoin

from bs4 import BeautifulSoup

TAGS = {  # noqa: WPS407
    'child_pages': '.department-item-link',
    'image_cards': '.administration-card',
    'images': '.administration-card-image > img',
    'title': '.administration-card-title',
}


def get_children(page):
    tag = TAGS['child_pages']
    soup = BeautifulSoup(page, 'html.parser')
    return (block['href'] for block in soup.select(tag))


def get_images(page):
    soup = BeautifulSoup(page, 'html.parser')
    image_cards = soup.select(TAGS['image_cards'])

    images = []
    for block in image_cards:
        url = block.select(TAGS['images'])[0]['src']
        text = block.select(TAGS['title'])[0].text
        text = unicodedata.normalize('NFKD', text)
        images.append((text, url))

    return images


def make_full_url(parent, child):
    return urljoin(parent, child)
