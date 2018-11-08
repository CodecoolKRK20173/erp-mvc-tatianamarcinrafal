""" Common functions for models
implement commonly used functions here
"""
import random


from model import data_manager
from model import common

def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    record.insert(0, generate_random(record))
    table.append(record)

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    for element in table:
        test = None
        if element[0] == id_:
            table.remove(element)
    return table


def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
    """
    record.insert(0, id_)
    for counter, value in enumerate(table):
        if value[0] == id_:
            table[counter] = record[:]
    return table
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
