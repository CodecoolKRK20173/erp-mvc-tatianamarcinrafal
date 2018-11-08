""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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

    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number

    """
    year_profit = {}
    for row in table:
        year = row[3]
        money = row[5]
        profit = row[4]
        if year not in year_profit.keys():
            if profit == "in":
                year_profit[year] = int(money)
            elif profit == "out":
                year_profit[year] = 0 - int(money)
        else:
            if profit == "in":
                year_profit[year] += int(money)
            elif profit == "out":
                year_profit[year] -= int(money)
    year_highest_profit = 0
    highest_profit = 0
    
    if year_profit:
        year_profit_list = tuple(year_profit.items())
        for pair in year_profit_list:
            if pair[1] > highest_profit:
                highest_profit = pair[1]
                year_highest_profit = pair[0] 
    
    if year_highest_profit:
        number = int(year_highest_profit)

    return number


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]
    (profit = in - out)
    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    profit_transaction = 0
    profit = []

    for row in table:
        year_transaction = int(row[3])
        amout_transaction = int(row[5])
        transaction = row[4]        
        if year_transaction == year:
            if transaction == "in":
                profit.append(amout_transaction)
            elif transaction == "out":
                profit.append(-(amout_transaction))                
    
    if profit:
        for amount in profit:
            profit_transaction += int(amount)
            
    if profit_transaction:
        amount_transaction = len(profit)
        average_profit = round(float(profit_transaction / amount_transaction), 3)
    
    return average_profit