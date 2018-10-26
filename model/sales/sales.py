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

    if len(str(month_from)) == 1:
        month_from = '0' + str(month_from)

    if len(str(day_from)) == 1:
        day_from = '0' + str(day_from)

    if len(str(day_to)) == 1:
        day_to = '0' + str(day_to)

    if len(str(month_to)) == 1:
        month_to = '0' + str(month_to)

    from_date = int(str(year_from)+str(month_from)+str(day_from))
    to_date = int(str(year_to)+str(month_to)+str(day_to))

    if from_date > to_date:
        from_date, to_date = to_date, from_date

    list_with_item_sold_between = []
    for item in table:
        if len(str(item[3])) == 1:
            day = '0' + str(item[3])
        else:
            day = str(item[3])
        if len(str(item[4])) == 1:
            month = '0' + str(item[4])
        else:
            month = str(item[4])

        item_date = int(item[5]+month+day)

        if item_date >= from_date and item_date <= to_date:
            list_with_item_sold_between.append(item)

    return list_with_item_sold_between

    # your code
