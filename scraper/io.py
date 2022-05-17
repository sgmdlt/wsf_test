import csv
import os


def get_files(directory):
    files = os.listdir(directory)
    return [
        {
            'filename': name,
            'path': _path(name, directory),
            'last_name': _prepare(name),
        }
        for name in files
        if len(name) > 2
    ]


def _path(name, directory):
    full_directory = os.path.abspath(directory)
    return os.path.join(full_directory, name)


def _prepare(filename):
    return filename.split('-')[0]


def get_data(file):
    with open(file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def filter_persons(data):
    persons = {}

    for row in data:
        name = row['person_name']
        info = {
            'income_year': row['income_year'],
            'person_id': row['person_id'],
            'section_id': row['section_id'],
            'position': row['position'],
            'department': row['department'],
        }

        if persons.get(name):
            if int(info['income_year']) > int(persons[name]['income_year']):
                persons[name] = info
        else:
            persons[name] = info
    return persons
