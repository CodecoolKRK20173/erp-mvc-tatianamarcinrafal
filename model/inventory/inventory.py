""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
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
    # your code

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

    # your code

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

    # your code

    return table


# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """
    table_with_available_items = []
    actual_year = 2018
    for record in table:
        durability_year = int(record[3])+int(record[4])
        if durability_year >= actual_year:
            table_with_available_items.append(record)

    return table_with_available_items

    # your code


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """
    dict_avg_durability = {}
    list_of_manufactures = []
    for record in table:
        list_of_manufactures.append(record[2])
    list_of_manufactures = set(list_of_manufactures)

    list_without_doble_manuf = []
    for manuf in list_of_manufactures:
        if manuf not in list_without_doble_manuf:
            list_without_doble_manuf.append(manuf)

    list_with_avg_durability = []
    for manufactures in list_without_doble_manuf:
        sum_durability = 0
        i = 0
        for record in table:
            if record[2] == manufactures:
                i += 1
                sum_durability += int(record[4])
        avg = sum_durability/i
        list_with_avg_durability.append(avg)

    for index in range(len(list_without_doble_manuf)):
        dict_avg_durability[list_without_doble_manuf[index]] = list_with_avg_durability[index]

    return dict_avg_durability
