# -*- coding: utf-8 -*-

from typing import Iterable, Optional

from wemake_python_styleguide import constants
from wemake_python_styleguide.options.defaults import MIN_VARIABLE_LENGTH


def is_wrong_variable_name(name: str, to_check: Iterable[str]) -> bool:
    """
    Checks that variable is not prohibited by explicitly listing it's name.

    >>> is_wrong_variable_name('wrong', ['wrong'])
    True

    >>> is_wrong_variable_name('correct', ['wrong'])
    False

    >>> is_wrong_variable_name('_wrong', ['wrong'])
    True

    >>> is_wrong_variable_name('wrong_', ['wrong'])
    True

    >>> is_wrong_variable_name('wrong__', ['wrong'])
    False

    >>> is_wrong_variable_name('__wrong', ['wrong'])
    False

    """
    for name_to_check in to_check:
        choices_to_check = [
            name_to_check,
            '_{0}'.format(name_to_check),
            '{0}_'.format(name_to_check),
        ]
        if name in choices_to_check:
            return True
    return False


def is_upper_case_name(name: Optional[str]) -> bool:
    """
    Checks that attribute name has no upper-case letters.

    >>> is_upper_case_name('camelCase')
    True

    >>> is_upper_case_name('UPPER_CASE')
    True

    >>> is_upper_case_name('camel_Case')
    True

    >>> is_upper_case_name('snake_case')
    False

    >>> is_upper_case_name('snake')
    False

    >>> is_upper_case_name('snake111')
    False

    >>> is_upper_case_name('__variable_v2')
    False

    >>> is_upper_case_name(None)
    False

    """
    return name is not None and any(character.isupper() for character in name)


def is_too_short_variable_name(
    name: Optional[str],
    min_length: int = MIN_VARIABLE_LENGTH,
) -> bool:
    """
    Checks for too short variable names.

    >>> is_too_short_variable_name('test')
    False

    >>> is_too_short_variable_name(None)
    False

    >>> is_too_short_variable_name('o')
    True

    >>> is_too_short_variable_name('_')
    False

    >>> is_too_short_variable_name('z1')
    False

    >>> is_too_short_variable_name('z', min_length=1)
    False

    """
    if name is None:
        return False

    return name != constants.UNUSED_VARIABLE and len(name) < min_length


def is_variable_name_with_underscored_number(name: str) -> bool:
    """
    Checks for variable names with underscored number.

    >>> is_variable_name_with_underscored_number('star_wars_episode2')
    False

    >>> is_variable_name_with_underscored_number(None)
    False

    >>> is_variable_name_with_underscored_number('come2_me')
    False

    >>> is_variable_name_with_underscored_number('_')
    False

    >>> is_variable_name_with_underscored_number('z1')
    False

    >>> is_variable_name_with_underscored_number('star_wars_episode_2')
    True

    >>> is_variable_name_with_underscored_number('come_2_me')
    True

    >>> is_variable_name_with_underscored_number('iso_123_456')
    False

    """
    pattern = constants.UNDERSCORED_NUMBER_PATTERN
    return name is not None and pattern.match(name) is not None