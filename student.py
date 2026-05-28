"""student.py

Contains the grade calculation logic and a simple OOP model for a student.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Student:
    """A Student object.

    OOP terminology (LO2):
    # Class: A blueprint for creating objects (Student).
    #Object: A specific instance created from a class (e.g., Student(name, mark)).
    # Method: A function defined on a class that operates on the object (calculate_grade()).

    Why OOP is useful here:
    # Grade rules and student data are kept together, making the program easy to extend
      (e.g., later add subjects, modules, or different assessment policies).
    # We can add more methods without rewriting the command-line workflow.
    """

    name: str
    mark: float

    def calculate_grade(self) -> str:
        """Calculate the grade string from the student's mark."""
        if self.mark < 0 or self.mark > 100:
            raise ValueError("Mark must be between 0 and 100 inclusive.")

        if 0 <= self.mark <= 39:
            return fail()
        if 40 <= self.mark <= 59:
            return pass_grade()
        if 60 <= self.mark <= 79:
            return merit()
        # 80-100
        return distinction()

    def as_dict(self) -> dict:
        """Return student details as a dictionary (useful for later expansion)."""
        return {
            "name": self.name,
            "mark": self.mark,
            "grade": self.calculate_grade(),
        }


# Grade rule functions

def fail() -> str:
    return "Fail"


def pass_grade() -> str:
    return "Pass"


def merit() -> str:
    return "Merit"


def distinction() -> str:
    return "Distinction" 























