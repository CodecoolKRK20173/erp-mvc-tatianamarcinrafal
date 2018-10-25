""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
from model import data_manager
from model import common


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    small_price = int(table[0][2])
    print(small_price)

    for price in table:
        if small_price >= int(price[2]):
            small_price = int(price[2])

    list_with_cheapest_games = []
    for record in table:
        if int(record[2]) == small_price:
            list_with_cheapest_games.append(record)

    def sort_list(list_with_title_from_file):

        iterations = 1
        N = len(list_with_title_from_file)
        j = 0
        while iterations < N:
            if j <= N-2:
                if list_with_title_from_file[j] > list_with_title_from_file[j+1]:
                    temp = list_with_title_from_file[j+1]
                    list_with_title_from_file[j+1] = list_with_title_from_file[j]
                    list_with_title_from_file[j] = temp
                    j = j + 1
                else:
                    j = j + 1
            else:
                iterations = iterations + 1
                j = 0

        return list_with_title_from_file

    if len(list_with_cheapest_games) == 1:
        return list_with_cheapest_games
    else:
        return sort_list(list_with_cheapest_games)[0]

    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
