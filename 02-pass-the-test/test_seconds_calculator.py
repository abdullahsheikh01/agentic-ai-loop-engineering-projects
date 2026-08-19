"""36 pytest tests describing the expected (correct) behaviour of the calculator.

These tests encode the specification. They are written against the FIXED
behaviour, so several currently fail against the buggy seconds_calculator.py -
fix the bugs in seconds_calculator.py until every test here passes.
"""

import pytest

from seconds_calculator import (
    add_seconds,
    format_seconds,
    hours_to_seconds,
    is_valid_time,
    minutes_to_seconds,
    parse_time,
    time_difference,
    to_seconds,
)


# --- to_seconds --------------------------------------------------------------

def test_to_seconds_basic():
    assert to_seconds(1, 30, 45) == 5445


def test_to_seconds_zero():
    assert to_seconds(0, 0, 0) == 0


def test_to_seconds_minutes_only():
    assert to_seconds(0, 5, 0) == 300


def test_to_seconds_seconds_only():
    assert to_seconds(0, 0, 42) == 42


def test_to_seconds_large():
    assert to_seconds(2, 0, 10) == 7210


# --- parse_time --------------------------------------------------------------

def test_parse_time_midnight():
    assert parse_time("00:00:00") == 0


def test_parse_time_noon():
    assert parse_time("12:00:00") == 43200


def test_parse_time_with_seconds():
    assert parse_time("01:02:03") == 3723


def test_parse_time_edge():
    assert parse_time("23:59:59") == 86399


def test_parse_time_bad_format_raises():
    with pytest.raises(ValueError):
        parse_time("12:00")


def test_parse_time_empty_raises():
    with pytest.raises(ValueError):
        parse_time("")


def test_parse_time_non_numeric_raises():
    with pytest.raises(ValueError):
        parse_time("ab:cd:ef")


# --- time_difference ---------------------------------------------------------

def test_time_difference_same_times():
    assert time_difference("12:00:00", "12:00:00") == 0


def test_time_difference_seconds_only():
    assert time_difference("00:00:00", "00:00:30") == 30


def test_time_difference_reverse_order():
    assert time_difference("00:00:30", "00:00:00") == 30


def test_time_difference_cross_hour():
    assert time_difference("01:00:00", "02:30:15") == 5415


def test_time_difference_large_gap():
    assert time_difference("00:00:00", "23:59:59") == 86399


def test_time_difference_reverse_large_gap():
    assert time_difference("02:30:15", "01:00:00") == 5415


def test_time_difference_across_midnight():
    assert time_difference("23:59:59", "00:00:01") == 86398


# --- format_seconds ----------------------------------------------------------

def test_format_seconds_zero():
    assert format_seconds(0) == "00:00:00"


def test_format_seconds_seconds_only():
    assert format_seconds(42) == "00:00:42"


def test_format_seconds_minutes():
    assert format_seconds(300) == "00:05:00"


def test_format_seconds_hours():
    assert format_seconds(3600) == "01:00:00"


def test_format_seconds_over_24_hours():
    assert format_seconds(90061) == "25:01:01"


def test_format_seconds_roundtrip():
    assert format_seconds(to_seconds(1, 2, 3)) == "01:02:03"


# --- is_valid_time -----------------------------------------------------------

def test_is_valid_time_valid():
    assert is_valid_time("12:30:45") is True


def test_is_valid_time_invalid_hour():
    assert is_valid_time("25:00:00") is False


def test_is_valid_time_invalid_minute():
    assert is_valid_time("12:60:00") is False


def test_is_valid_time_invalid_second():
    assert is_valid_time("12:30:61") is False


def test_is_valid_time_bad_separator():
    assert is_valid_time("12-30-45") is False


# --- add_seconds -------------------------------------------------------------

def test_add_seconds_basic():
    assert add_seconds("12:00:00", 30) == "12:00:30"


def test_add_seconds_wraps_after_midnight():
    assert add_seconds("23:59:59", 2) == "00:00:01"


def test_add_seconds_full_day_wraps():
    assert add_seconds("12:00:00", 86400) == "12:00:00"


def test_add_seconds_across_midnight():
    assert add_seconds("23:30:00", 3600) == "00:30:00"


# --- unit helpers ------------------------------------------------------------

def test_minutes_to_seconds():
    assert minutes_to_seconds(5) == 300


def test_hours_to_seconds():
    assert hours_to_seconds(2) == 7200