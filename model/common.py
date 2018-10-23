""" Common functions for models
implement commonly used functions here
"""
import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    def guess_upper_letter():
        return random.choice('abcdefghijklmnopqrstuvwxyz').upper()

    def guess_letter():
        return random.choice('abcdefghijklmnopqrstuvwxyz')

    def guess_int():
        return random.randint(1, 9)

    a = str(guess_letter())
    b = str(guess_upper_letter())
    c = str(guess_int())
    d = str(guess_int())
    e = str(guess_upper_letter())
    f = str(guess_letter())
    generated = a + b + c + d + e + f + '#&'

    for lines in table:
        if lines[0] == generated:
            return generate_random(table)

    return generated


# def add_item(table, list_labels):
#     get
