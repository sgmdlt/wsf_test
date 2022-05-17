import argparse

from scraper.loader import DEFAULT_URL

def get_args():
    parser = argparse.ArgumentParser(
        prog='minobr photo scraper',
        description='Download photos of employes from site of ministry of education',
        usage='scraper <table>',
    )
    parser.add_argument(
        'table',
        help='table with names for renaming',
        type=str,
    )

    args = parser.parse_args()
    return args.table
