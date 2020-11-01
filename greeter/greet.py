"""
A simple program to greet people to the class.
"""
import inspect

from greeter import people


def find_people():
    """
    Returns the functions prefixed with `get`.
    """
    functions = inspect.getmembers(people, predicate=inspect.isfunction)
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
    people_list = find_people()
    print(get_welcome_message(people_list))


if __name__ == "__main__":
    """
    Main entry point of the program.
    """
    greet_people()
