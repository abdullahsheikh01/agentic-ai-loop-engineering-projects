"""A Seconds Calculator.

Give it two different clock times and it calculates the difference between
them in seconds. Runs WITHOUT any user input - two times are hard-coded in
main() to demonstrate the functions.

BUGS: This file intentionally contains bugs. Find them and fix them so that
all 36 tests in test_seconds_calculator.py pass.
"""


def to_seconds(hours, minutes, seconds):
    """Convert hours, minutes and seconds into a total number of seconds."""
    return hours * 3600 + minutes * 60 + seconds


def minutes_to_seconds(minutes):
    """Convert minutes to seconds."""
    return minutes * 60


def hours_to_seconds(hours):
    """Convert hours to seconds."""
    return hours * 3600


def parse_time(time_str):
    """Parse a "HH:MM:SS" string into a total number of seconds.

    Raises ValueError when the string is not in the form HH:MM:SS.
    """
    parts = time_str.split(":")
    if len(parts) != 3:
        raise ValueError("invalid time format")
    hours, minutes, seconds = int(parts[0]), int(parts[1]), int(parts[2])
    return hours * 3600 + minutes * 60 + seconds


def time_difference(time_a, time_b):
    """Return the absolute difference between two "HH:MM:SS" times in seconds."""
    return abs(parse_time(time_b) - parse_time(time_a))


def format_seconds(total):
    """Format a total number of seconds as "HH:MM:SS" (hours may exceed 24)."""
    hours = total // 3600
    minutes = (total % 3600) // 60
    seconds = total % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def is_valid_time(time_str):
    """Return True when time_str is a valid "HH:MM:SS" clock time.

    Valid hours are 0-23, valid minutes and seconds are 0-59.
    """
    try:
        hours, minutes, seconds = (int(x) for x in time_str.split(":"))
    except ValueError:
        return False
    return hours <= 23 and minutes <= 59 and seconds <= 59


def add_seconds(time_str, seconds):
    """Add seconds to a "HH:MM:SS" time and return the result as "HH:MM:SS".

    The result wraps around after 24 hours.
    """
    total = (parse_time(time_str) + seconds) % 86400
    total_hours = total // 3600
    minutes = (total % 3600) // 60
    remaining = total % 60
    return f"{total_hours:02d}:{minutes:02d}:{remaining:02d}"


def main():
    t1 = "14:30:00"
    t2 = "15:45:30"
    print(f"{t1} vs {t2}: {time_difference(t1, t2)} seconds")


if __name__ == "__main__":
    main()