import logging
import string
import traceback
from random import sample

from scraper.exceptions import FileSystemError

logger = logging.getLogger(__name__)


def local_name(name, ext=''):

    path = _generate(name)

    return '{0}{1}'.format(path, ext)


def _generate(name):
    name = name.strip()
    if name:
        return name.replace('/', '-').replace(' ', '-')
    return 'noname_{0}'.format(_random_name())


def _random_name():
    digits_letters = string.ascii_letters + string.digits
    return ''.join(sample(digits_letters, 6))


def save(source, path, mode='wb'):
    try:
        with open(path, mode=mode) as out:
            out.write(source)
    except IOError as exc:
        logger.debug(traceback.format_exc(2, chain=False))
        logger.error('No permission to directory')
        raise FileSystemError() from exc
    logger.info('{0} was saved successfully'.format(path))
    return path
