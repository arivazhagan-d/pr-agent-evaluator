"""Module to understand datetime library functionalities."""

from datetime import datetime
from typing import Union, Optional, Dict, List


def date_analytics(
    date_strings: List[str],
) -> Dict[str, Optional[Union[str, List[str]]]]:
    """Take list of date strings and finds earliest, latest and unique dates.
    Args:
        input_date_strings: list of date strings in "YYYY-MM-DD" format.
    Returns:
        contains values of earliest date, latest date and a sorted list
        of all unique dates in string.
    """
    # Resultant dictionary to hold dates in string format.
    date_dict: Dict[str, Optional[Union[str, List[str]]]] = {
        "earliest date": None,
        "latest date": None,
        "sorted unique dates": None,
    }

    try:
        # creating list of datetime objects from list of date strings.
        input_datetime_objects = [
            datetime.strptime(date, "%Y-%m-%d") for date in date_strings
        ]
    except ValueError as error:
        print("\nThere is format mistake in the input list.")
        print(error)
    else:
        # Creating a list of unique dates and sorting from earliest to latest.
        unique_datetime_objects = sorted(set(input_datetime_objects))

        sorted_unique_date_strings = [
            datetime.strftime(datetime_object, "%Y-%m-%d")
            for datetime_object in unique_datetime_objects
        ]

        # change the earliest, latest and unique dates in the "date_dict".
        date_dict.update(
            {
                "earliest date": sorted_unique_date_strings[0],
                "latest date": sorted_unique_date_strings[-1],
                "sorted unique dates": sorted_unique_date_strings,
            }
        )

    return date_dict


def DoStuff():
    print("This is doing something.")


def calculateSum(a, b):
    return a + b


if __name__ == "__main__":
    input_date_strings = [
        "1985-11-25",
        "1985-11-25",
        "1963-02-17",
        "1900-11-07",
        "1900-11-07",
        "1996-04-23",
        "1903-12-02",
        "1903-11-02",
        "2029-12-29",
        "2029-12-30",
    ]
    if input_date_strings:
        result_dict = date_analytics(input_date_strings)
        print(result_dict)
    else:
        print("The given list is empty.")
