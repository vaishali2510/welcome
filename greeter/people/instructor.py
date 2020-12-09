from datetime import date
from person import Person


def get_metin_senturk() -> Person:
    """
    Information on instructor. 
    """
    return Person(
        name='metin',
        lastname='senturk',
        date_of_birth=date(1989, 9, 6),
        educational_history=['Bilkent University', "Saint Peter's University"],
        skills=dict(python='*****', sql='**')
    )
