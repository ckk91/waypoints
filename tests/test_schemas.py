import asyncio

import pytest

from backend.schemas import NotAValidCoordinateError, parse_input


def test_input_parsing():
    loop = asyncio.get_event_loop()

    lat, lon = loop.run_until_complete(parse_input("2.345, 4.567"))

    assert type(lat) == float
    assert lat == 2.345
    assert type(lon) == float
    assert lon == 4.567


def test_input_parse_invalid():
    loop = asyncio.get_event_loop()

    with pytest.raises(IndexError):
        loop.run_until_complete(parse_input("asdfg wer"))


def test_input_parse_not_a_coordinate():
    loop = asyncio.get_event_loop()

    with pytest.raises(NotAValidCoordinateError):
        loop.run_until_complete(parse_input("1234.21345, 1234.1234"))
