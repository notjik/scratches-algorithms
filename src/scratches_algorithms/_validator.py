"""
A module for validating passed values during function operation.

-----

:author: notjik:
:license: MIT License
:copyright: (c) 2023 notjik
"""
from typing import Sequence


def _is_valid_bool(*data: bool) -> None:
    """
    A special void function for checking logical type parameters.
    :param data: tuple of passed values to check
    :raise: TypeError if the type does not match the boolean
    """
    for elem in data:
        if not isinstance(elem, bool):
            raise TypeError('The current {} type is {}, expected bool'.format(data, type(data).__name__))
    return None


def _is_valid_int(*data: int) -> None:
    """
    A special void function for checking integer type parameters
    :param data: tuple of passed values to check
    :raise: TypeError if the type does not match the integer
    """
    for elem in data:
        if not isinstance(elem, int) or isinstance(elem, bool):
            raise TypeError('The current {} type is {}, expected int'.format(elem, type(elem).__name__))
    return None


def _is_valid_sequence(*data: Sequence, closed: Sequence = None) -> None:
    """
    A special void function for checking parameters for belonging to sequences
    :param data: tuple of passed values to check
    :param closed: optional argument of sequences from forbidden sequence types
    :raise: TypeError if the type does not belong to sequences
    """
    if closed is None:
        closed = []
    for elem in data:
        if not isinstance(elem, Sequence) or any((isinstance(elem, closed_type) for closed_type in closed)):
            raise TypeError(
                'The current {} type is {}, any sequence is expected{}'.format(
                    elem,
                    type(elem).__name__,
                    ' except {}'.format(*closed) if closed else ''))
    return None
