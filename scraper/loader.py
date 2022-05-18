from concurrent import futures
import logging
import os
import traceback

import requests
from scraper import html
from scraper.exceptions import NetworkError
from scraper.storage import local_name, save

DEFAULT_DIR = os.getcwd()
DEFAULT_URL = 'https://minobrnauki.gov.ru/about/deps/'

logger = logging.getLogger(__name__)


def loader(url, directory):
    page_name = local_name(url, ext='.html')
    page_path = os.path.join(directory, page_name)
    dir_path = os.path.join(directory, 'deps_photos')

    parent_page = get_content(url)
    os.makedirs(dir_path, exist_ok=True)
    logger.info('page path - {0}, dir path - {1}'.format(page_path, dir_path))
    save(parent_page, page_path)
    logger.info('Page saved!')

    relevant_child_urls = html.get_children(parent_page)
    full_child_urls = (html.make_full_url(url, child) for child in relevant_child_urls)  # noqa: E501
    download_images(full_child_urls, dir_path)

    return dir_path


def download_images(urls, dir_path):
    images = []
    with futures.ThreadPoolExecutor(max_workers=8) as executor:
        tasks = [(executor.submit(get_content, url), url) for url in urls]
        result = [(task.result(), url) for task, url in tasks]
        logging.info(f"All adresses was scanned")
    
    for page, url in result:
        for title, image_url in html.get_images(page):
            full_url = html.make_full_url(url, image_url)
            images.append((title, full_url))
        logger.info(images)

    with futures.ThreadPoolExecutor(max_workers=8) as executor:
        tasks = [executor.submit(get_and_save_image, title, url, dir_path) for title, url in images]    
        result = [task.result() for task in tasks]
        logging.info(f"All photos was downloaded")
    

def get_and_save_image(title, url, dir_path): 
    image = get_content(url)
    local_path = os.path.join(dir_path, local_name(title))
    logger.info('Image path - {0}'.format(local_path))
    save(image, local_path, 'wb')


def get_content(url):
    try:  # noqa: WPS229
        response = requests.get(url)
        response.raise_for_status()
        logger.info('Got content {0}'.format(url))

    except requests.exceptions.RequestException as exp:
        logger.debug(traceback.format_exc(2, chain=False))
        logger.error('Cannot download page: {0} \n{1}'.format(
            url,
            traceback.format_exc(0, chain=False),
        ))
        raise NetworkError from exp

    return response.content
