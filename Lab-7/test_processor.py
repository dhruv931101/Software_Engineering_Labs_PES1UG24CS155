"""Hypothesis properties for the three Lab 7 input-processing functions."""

import os

import pytest
from hypothesis import given, settings, strategies as st

if os.environ.get("LAB7_USE_ORIGINAL") == "1":
    from processor_original import parse_ticket_id, speed_excess, total_fines
else:
    from processor import parse_ticket_id, speed_excess, total_fines


@settings(max_examples=200, deadline=None, derandomize=True)
@given(
    prefix=st.text(
        alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        min_size=1,
        max_size=10,
    ),
    year=st.integers(min_value=1, max_value=9999),
    serial=st.integers(min_value=0, max_value=9_999_999_999),
)
def test_parse_ticket_id_returns_normalized_components(prefix, year, serial):
    ticket = f"{prefix}-{year:04d}-{serial}"
    assert parse_ticket_id(ticket) == (prefix.upper(), year, serial)


@settings(max_examples=200, deadline=None, derandomize=True)
@given(
    prefix=st.text(
        alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        min_size=1,
        max_size=10,
    ),
    serial=st.integers(min_value=0, max_value=9_999_999_999),
)
def test_parse_ticket_id_rejects_zero_year(prefix, serial):
    with pytest.raises(ValueError):
        parse_ticket_id(f"{prefix}-0000-{serial}")


@settings(max_examples=100, deadline=None, derandomize=True)
@given(parts=st.lists(st.text(), min_size=1, max_size=5))
def test_parse_ticket_id_rejects_unicode_and_wrong_separators(parts):
    with pytest.raises(ValueError):
        parse_ticket_id("/".join(parts))


@settings(max_examples=150, deadline=None, derandomize=True)
@given(amounts=st.lists(st.integers(min_value=0, max_value=10**30), max_size=100))
def test_total_fines_sums_nonnegative_amounts_and_caps(amounts):
    csv_value = " , ".join(str(amount) for amount in amounts)
    assert total_fines(csv_value) == min(sum(amounts), 10000)


def test_total_fines_treats_empty_and_whitespace_as_zero():
    assert total_fines("") == 0
    assert total_fines(" \t ") == 0


@settings(max_examples=100, deadline=None, derandomize=True)
@given(amount=st.integers(min_value=0, max_value=10**20))
def test_total_fines_rejects_negative_amounts(amount):
    with pytest.raises(ValueError):
        total_fines(f"{amount},-1")


@settings(max_examples=100, deadline=None, derandomize=True)
@given(token=st.text())
def test_total_fines_rejects_unicode_or_malformed_tokens(token):
    with pytest.raises(ValueError):
        total_fines(f"\u2603{token}")


@settings(max_examples=200, deadline=None, derandomize=True)
@given(
    speed=st.integers(min_value=0, max_value=10**30),
    limit=st.integers(min_value=1, max_value=10**30),
)
def test_speed_excess_is_nonnegative_and_matches_integer_percentage(speed, limit):
    expected = 0 if speed <= limit else (speed - limit) * 100 // limit
    assert speed_excess(f" {speed} / {limit} ") == expected


@settings(max_examples=100, deadline=None, derandomize=True)
@given(speed=st.integers(min_value=0, max_value=10**20))
def test_speed_excess_rejects_zero_limit(speed):
    with pytest.raises(ValueError):
        speed_excess(f"{speed}/0")


@settings(max_examples=100, deadline=None, derandomize=True)
@given(speed=st.integers(min_value=0, max_value=10**20))
def test_speed_excess_rejects_negative_speed(speed):
    with pytest.raises(ValueError):
        speed_excess(f"-{speed}/60")


@settings(max_examples=100, deadline=None, derandomize=True)
@given(value=st.text())
def test_speed_excess_rejects_malformed_unicode_readings(value):
    with pytest.raises(ValueError):
        speed_excess(f"\u2603{value}/60")


@pytest.mark.parametrize(
    "function_and_value",
    [(parse_ticket_id, None), (total_fines, None), (speed_excess, None)],
)
def test_all_functions_reject_none(function_and_value):
    function, value = function_and_value
    with pytest.raises(TypeError):
        function(value)
