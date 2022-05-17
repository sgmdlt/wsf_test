import os
import pytest
from scraper.io import get_files
from scraper.rename import run
from tests.utils import get_fixture

FILES = [
    'Трубников-Григорий-Владимирович',
    'Боровская-Марина-Александровна',
    'Мясников-Олег-Олегович',
    'Пыжкин-Петр-Петрович',
    '-',
    'Кузьмин-Сергей-Владимирович',
    'Медведев-Анатолий-Михайлович',
]


VALID_FILES = [
    'Трубников-Григорий-Владимирович',
    'Боровская-Марина-Александровна',
    'Мясников-Олег-Олегович',
    'Пыжкин-Петр-Петрович',
    'Кузьмин-Сергей-Владимирович',
    'Медведев-Анатолий-Михайлович',
]

@pytest.fixture
def table():
    return get_fixture('name_list.csv')  


def test_get_files(tmpdir):
    for file in FILES:
        with open(os.path.join(tmpdir, file), 'w'):
            pass
    valid_files = get_files(tmpdir)
    filenames = (file['filename'] for file in valid_files)
    assert sorted(filenames) == sorted(VALID_FILES)