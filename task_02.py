#!usr/bin/env python
# -*- coding: utf-8 -*-
""" W6 Task 02 """

import data
import task_01

def get_average(numbers=[]):
    """
    Return the average of the arguments.
    :param numbers:
    :return average as float:
    """
    sum = 0.0
    for number in numbers:
        sum += number
    avg = float(float(sum) / len(numbers))
    return avg

TOTAL_AVG = get_average(data.TASK_O1)
EVEN_AVG = get_average(task_01.evens_and_odds(data.TASK_O1, True))
ODD_AVG = get_average(task_01.evens_and_odds(data.TASK_O1, False))

REPORT ="""
    Task 02 Report
    -------------------------------
    Total AVG: {}
    Even AVG:  {}
    Odd AVG:   {}
"""

print REPORT.format(TOTAL_AVG, EVEN_AVG, ODD_AVG)