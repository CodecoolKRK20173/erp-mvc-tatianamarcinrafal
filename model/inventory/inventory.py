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
    actual_year = 2017
    for record in table:
        durability_year = int(record[3])+int(record[4])

        if durability_year >= actual_year:
            record[3] = int(record[3])
            record[4] = int(record[4])
            table_with_available_items.append(record)

    return table_with_available_items


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
