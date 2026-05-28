"""main.py

Command-line program to manage student results.

- Takes input from the command line OR prompts interactively if missing.
- Asks for student name and student mark.
- Calculates and displays grade.
- Includes simple error handling.
"""

from __future__ import annotations

import sys

from tabulate import tabulate
from colorama import Fore, Style, init as colorama_init

colorama_init(autoreset=True)


from student import Student
from utils import parse_mark, prompt_non_empty, validate_mark



def usage() -> str:
    return (
        "Usage: python main.py [student_name mark]\n"
        "If name/mark are not provided, the program will prompt you."
    )


def get_cli_args() -> tuple[str | None, str | None]:
    """Return (name, mark) from CLI arguments if provided."""
    # argv[0] is the script name
    if len(sys.argv) >= 3:
        return sys.argv[1], sys.argv[2]
    return None, None




def prompt_for_student(default_name: str | None = None) -> Student:
    name = prompt_non_empty(
        f"Enter student name [{default_name}]: " if default_name else "Enter student name: "
    )

    # If user just presses enter at the name prompt, use the default.
    if default_name and name == "":
        name = default_name

    while True:
        raw_mark = input("Enter student mark (0-100): ").strip()
        try:
            mark = validate_mark(parse_mark(raw_mark))
            return Student(name=name, mark=mark)
        except ValueError as e:
            # Error handling example: invalid input (text instead of a number)
            print(f"Invalid mark: {e}")



def main() -> int:
    name_arg, mark_arg = get_cli_args()

    # If missing command-line args, handle by prompting interactively.
    if name_arg is None or mark_arg is None:
        student = prompt_for_student()
    else:
        # If args were provided, use them directly.
        # (We still validate mark; name is expected to be a non-empty string.)
        try:
            # Do not re-prompt for name when provided via CLI.
            name = name_arg
            if not name:
                name = prompt_non_empty("Enter student name: ")

            mark = validate_mark(parse_mark(mark_arg))
            student = Student(name=name, mark=mark)

        except ValueError as e:
            print(f"Invalid input: {e}")
            print(usage())
            return 2
        except Exception:
            print("Unexpected error. Please try again.")
            return 2


    # Prepare output
    details = student.as_dict()
    headers = ["Student Name", "Mark", "Grade"]
    table = [[details["name"], details["mark"], details["grade"]]]

    print("\nStudent Result\n" + "-" * 15)
    print(tabulate(table, headers=headers, tablefmt="github"))


    # Use standard library + third-party library for a colored summary line
    import datetime

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    summary = f"Checked at {now}"
    print(Fore.CYAN + summary + Style.RESET_ALL)


    return 0


if __name__ == "__main__":
    raise SystemExit(main())


