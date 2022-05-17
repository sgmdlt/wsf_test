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
    first_part, *_ = filename.split('-')
    return first_part


def get_data(file):
    with open(file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


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