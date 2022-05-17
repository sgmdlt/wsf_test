import logging

CONFIGS = {  # noqa: WPS407
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # noqa: WPS323, E501
    'level': 'INFO',
    'handlers': [
        logging.StreamHandler(),
        logging.FileHandler('app.log'),
    ],
}


def setup_logger():
    logging.basicConfig(
        level=CONFIGS['level'],
        format=CONFIGS['format'],
        handlers=CONFIGS['handlers'],
    )
