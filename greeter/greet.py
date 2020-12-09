"""
A simple program to greet people to the class.
"""
import inspect
import pathlib
import importlib.util


def import_module_from_path(filepath):
    """
    Import a module from given path.
    https://stackoverflow.com/a/67692/5159551
    """
    spec = importlib.util.spec_from_file_location('person', filepath)
    person_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(person_module)
    return person_module


def find_people(person_module):
    """
    Returns the functions prefixed with `get` from a module.
    """
    functions = inspect.getmembers(person_module, predicate=inspect.isfunction)
    people_functions = filter(lambda x: x[0].startswith('get'), functions)

    persons = []
    for _, function in people_functions:
        person = function()
        persons.append(person)
    return persons


def get_welcome_message(people_list):
    """
    Prints a welcome message for a list of people. 
    """
    welcome = 'Welcome to the DS-542!\n'
    return welcome + '\n'.join(str(person) for person in people_list)


def greet_people():
    """
    Greet a participants of this project.
    """
    people_list = []
    for path_to_module in pathlib.Path(__file__).parent.glob('people/*.py'):
        person_module = import_module_from_path(path_to_module)
        module_people_list = find_people(person_module)
        people_list.extend(module_people_list)

    print(get_welcome_message(people_list))


if __name__ == "__main__":
    """
    Main entry point of the program.
    """
    greet_people()
