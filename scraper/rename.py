import logging
import os

from scraper.io import filter_persons, get_data, get_files

logger = logging.getLogger(__name__)


def run(directory, names_source):
    files_with_meta = get_files(directory)
    persons = filter_persons(get_data(names_source))
    filenames = rename(files_with_meta, persons)
    rewrite(filenames)
    return directory


def rename(filenames, persons):  # noqa: WPS231

    for file in filenames:
        for person, info in persons.items():
            if file['last_name'] in person:
                person_id = info.get('person_id')
                section_id = info.get('section_id')

                if person_id and person_id != 'NULL':
                    new_name = person_id
                else:
                    new_name = 'section_{0}'.format(section_id)

                new_path = _change_path(file['path'], new_name)
                file['new_path'] = new_path

    return filenames


def _change_path(old_path, new_name):
    parent_dir = os.path.abspath(os.path.join(old_path, os.pardir))
    return os.path.join(parent_dir, new_name)


def rewrite(files):
    for file in files:
        old_path = file.get('path')
        new_path = file.get('new_path')
        if new_path:
            os.rename(old_path, '{0}.jpg'.format(new_path))
            logger.info('File {0} was renamed to {1}'.format(old_path, new_path))  # noqa: E501
