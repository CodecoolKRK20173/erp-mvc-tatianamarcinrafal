""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
"""

# everything you'll need is imported:
# User interface module
import view
# data manager module
# common module
from controller import common
from view import terminal_view
from model import data_manager
import os

sales_file = "model/sales/sales.csv"
customers_file = "model/crm/customers.csv"

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    options = ["Add", "Remove", "Update", "Lowest price item ID", "Items sold between[in progress]"]
    common_options = ["Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
    file = "model/sales/sales.csv"
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year", "Crm ID"]
    choice = None
    dont_clear = False
    options_which_no_table_show = ['4', '5']
    while choice != '0':
        if not dont_clear:
            os.system("clear")
            table = data_manager.get_table_from_file(file)
            terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice_submenu(options)
        dont_clear = False
        if choice not in options_which_no_table_show:
            terminal_view.print_table(table, title_list)
        if choice == '1':
            add(file, common_options)
        if choice == '2':
            remove(file)
        if choice == '3':
            update(file, common_options)
        if choice == '4':
            lowest_price = sales.get_lowest_price_item_id(table)
            terminal_view.print_result(lowest_price, 'Lowest price game is: ')
            dont_clear = True
        if choice == '5':
            os.system("clear")
            dates_to_input = ['From month: ', 'From day: ', 'From year: ', 'To month:', 'To day: ', "To year: "]
            inputs = terminal_view.get_inputs(dates_to_input, "Please input appropriate data.")
            answer = sales.get_items_sold_between(table, int(inputs[0]), int(inputs[1]), int(inputs[2]), int(inputs[3]),
                                         int(inputs[4]), int(inputs[5]))
            terminal_view.print_table(answer, title_list)
            dont_clear = True



def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code


def add(table, common_options):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    common.get_table_from(sales_file)
    add_options = ["Add for an existing user", "Add new user"]
    os.system("clear")
    #terminal_view.print_menu("Please select an option:",add_options, "Return to main menu")
    adding_type = terminal_view.get_choice_submenu(add_options)
    if adding_type == '1':
        terminal_view.get_inputs(["Crm ID: "], "Please provide existing user ID")
        #terminal_view
    record = terminal_view.get_inputs([opt for opt in common_options], "Please provide following data: ")
    save(file, common.add(get_table_from(sales_file), record)) 
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

    common.remove(sales_file)

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    common.remove(sales_file)
    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):

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
        return list_with_cheapest_games[0][0]
    else:
        return sort_list(list_with_cheapest_games)[0][0]



def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

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

# functions supports data abalyser
# --------------------------------


def get_title_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_title_by_id_from_table(table, id):
    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _title_ of the item that was sold most recently.
    """

    # your code


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """

    # your code


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """

    # your code


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """

    # your code


def get_all_sales_ids_for_customer_ids_form_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code
