import sys

from scraper import cli
from scraper.exceptions import FileSystemError, NetworkError
from scraper.loader import loader, DEFAULT_DIR, DEFAULT_URL
from scraper.logging import setup_logger
from scraper.rename import run as rename


def main():
    table = cli.get_args()
    setup_logger()
    try:
        directory = loader(DEFAULT_URL, DEFAULT_DIR)
    except (NetworkError, FileSystemError):
        sys.exit(1)
    resulted_dir =  rename(directory, table)
    print(resulted_dir)


if __name__ == '__main__':
    main()
