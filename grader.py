"""
Grader module to evaluate letter grade from students' collective scores.
"""


def convert_points_to_letter(point):
    """
    Converts a given point to a letter grade.

    Parameters:
    A number in range of 0 to 100.

    Returns:
    Letter grade.
    """
    if point >= 94:
        grade = 'A'
    elif point >= 87 and point < 94:
        grade = 'A-'
    elif point >= 83 and point < 86:
        grade = 'B+'
    elif point >= 80 and point < 83:
        grade = 'B'
    elif point >= 77 and point < 80:
        grade = 'B-'
    elif point >= 73 and point < 77:
        grade = 'C'
    elif point >= 67 and point < 73:
        grade = 'C-'
    elif point in range(60, 67):
        grade = 'D'
    else:
        grade = 'F'

    return grade


def calculate_letter_grade(assignments: list, final_project: int, midterm: int, **kwargs):
    """
    Calculates a letter grade based on student scores.

    Parameters:
    assignments   - A list of student scores 
    final_project - Final project score
    return_grade  - Returns letter grade if True.

    Returns:
    A grade from the letter grade scale.
    """
    # weights
    pct_assignment = kwargs.get('pct_assignment', 0.50)
    pct_midterm = kwargs.get('pct_midterm', 0.20)
    pct_final_project = kwargs.get('pct_final_project', 0.30)

    # if bonus is given
    if len(assignments) == 6:
        lowest_score = min(assignments)
        lowest_index = assignments.index(lowest_score)
        assignments.pop(lowest_index)

    # points earned
    points_assignments = (sum(assignments) / len(assignments)) * pct_assignment
    points_midterm = midterm * pct_midterm
    points_final_project = final_project * pct_final_project

    # getting final points
    total_points = round(
        points_assignments + points_midterm + points_final_project, 1)

    if kwargs.get('return_grade', True):
        return convert_points_to_letter(total_points)

    return total_points


if __name__ == "__main__":

    # example
    grade = calculate_letter_grade(
        assignments=[100, 100, 100, 90, 60, 100],
        final_project=90,
        midterm=90,
        return_grade=False
    )

    # grade should be A- (92.0).
    print(grade)
