""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
from model import data_manager
from model import common
import os
from view import terminal_view

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

    # your code


    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """
    longest = 0
    user_id = ""
    for row in table:
        name = row[1]
        name = len(str(name))
        if name > longest:
            longest = name
            user_id = str(row[0])
    the_same_longest_name = []
    user_id_longest_name = []
    if longest != 0:
        for row in table:
            name = row[1]
            id_ = row[0]
            if len(str(name)) == longest:
                the_same_longest_name.append(str(name))
                user_id_longest_name.append(str(id_))
    if the_same_longest_name and user_id_longest_name:
        name_id = list(zip(the_same_longest_name,user_id_longest_name))
        id_alph_name = ""
        alph_name = ""
        for pair in name_id:
            longest_name = pair[0]
            longest_id = pair[1]
            if longest_name > alph_name:
                alph_name = longest_name
                id_alph_name = longest_id

    return id_alph_name


    # your code


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """
    list_subscribed = []
    for row in table:
        subscribed = row[3]
        number = str(1)
        subscription = "1"       
        if subscription in subscribed:
            name = str(row[1])
            email = str(row[2])
            customers = []
            customers.append(email)
            customers.append(name)
            list_subscribed.append(customers)
    return list_subscribed

    # your code


# functions supports data analyser
# --------------------------------


def get_name_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """
    answer = ''
    link_for_csv = "model/crm/customers.csv"
    table = data_manager.get_table_from_file(link_for_csv) 
    for row in table:
        id_customer = str(row[0])
        name_customer = str(row[1])
        if id == id_customer:
            answer = name_customer
        else:
            answer = None
    return answer



def get_name_by_id_from_table(table, id):
    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """
    for row in table:
        id_customer = str(row[0])
        name_customer = str(row[1])
        if id == id_customer:
            answer = name_customer
        else:
            answer = None
    return answer
    # your code
