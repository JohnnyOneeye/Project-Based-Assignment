"""utils.py

Helper functions for validating and parsing user input.

This keeps main.py clean and makes the project easier to expand.
"""

from __future__ import annotations


def parse_mark(value: str) -> float:
    """Parse a mark from a string to a float.

    Raises:
        ValueError: if the input cannot be converted to a number.
    """
    value = value.strip()
    return float(value)


def validate_mark(mark: float) -> float:
    """Validate mark is within 0-100.

    Raises:
        ValueError: if mark is outside the valid range.
    """
    if mark < 0 or mark > 100:
        raise ValueError("Mark must be between 0 and 100 inclusive.")
    return mark


def prompt_non_empty(prompt: str) -> str:
    """Prompt until the user enters a non-empty value."""
    while True:
        result = input(prompt).strip()
        if result:
            return result
        print("Please enter a non-empty value.")
        

