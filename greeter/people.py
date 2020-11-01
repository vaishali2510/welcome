"""
A list of students partipating to the class.
"""
from dataclasses import dataclass


@dataclass
class Person:
    """
    A representation of a person.
    """
    name: str
    lastname: str

    def __repr__(self) -> str:
        return '{}, {}'.format(self.lastname.capitalize(), self.name.capitalize())


def get_metin_senturk() -> Person:
    """
    Information on instructor. 
    """
    return Person(name='metin', lastname='senturk')
