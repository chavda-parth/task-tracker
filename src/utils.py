from typing import Any


def validate_type(name: str, value: Any, expected_type: type):
    actual_type = type(value)
    if actual_type is not expected_type:
        raise TypeError(f'{name} must be of type {expected_type.__name__} but is {actual_type.__name__}')