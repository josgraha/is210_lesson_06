#!usr/bin/env python
# -*- coding: utf-8 -*-
""" W6 Task 03 """

import data


def bubble_sort(items=[]):
    """
    Returns a sorted list.
    :param items:
    :return list:
    """
    length = len(items) - 1
    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(length):
            if items[i] > items[i+1]:
                temp = items[i] # swap elements
                items[i] = items[i+1]
                items[i+1] = temp
                isSorted = False
    return items