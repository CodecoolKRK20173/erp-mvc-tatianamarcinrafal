""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
from model import data_manager
from model import common


# special functions:
# ------------------


def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    dict = {}
    for element in table:
        if element[2] not in dict:
            dict[element[2]] = 0
        if element [2] in dict:
            dict[element[2]] += 1
    return dict 



def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
    sum_amount = 0
    times_summed = 0
    for element in table:
        if element[2] == manufacturer:
            sum_amount += int(element[4])
            times_summed += 1
    if times_summed != 0:
        return sum_amount/times_summed
