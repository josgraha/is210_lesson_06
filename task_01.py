#!usr/bin/env python
# -*- coding: utf-8 -*-
""" W6 Task 01 """

import data


def evens_and_odds(numbers=[], show_even=True):
    """
    Filters a list from numbers that matches show_even argument.
    :param numbers:
    :param show_even:
    :return boolean:
    """
    ret = []
    for i in numbers:
        if show_even:
            if not i % 2:
                ret.append(i)
        else:
            if i % 2:
                ret.append(i)
    return ret