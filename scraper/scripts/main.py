import logging
import sys

from scraper import cli
from scraper.exceptions import FileSystemError, NetworkError
from scraper.loader import DEFAULT_DIR, DEFAULT_URL, loader
from scraper.logging import setup_logger
from scraper.rename import run as rename

setup_logger()
logger = logging.getLogger(__name__)


def main():
    table = cli.get_args()
    try:
        directory = loader(DEFAULT_URL, DEFAULT_DIR)
    except (NetworkError, FileSystemError):
        sys.exit(1)
    resulted_dir = rename(directory, table)
    logger.info(resulted_dir)


if __name__ == '__main__':
    main()
