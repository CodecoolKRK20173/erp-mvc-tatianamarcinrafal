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
    os.system("clear")
    record.insert(0, common.generate_random(record))
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
    os.system("clear")
    for row in table:
        test = None
    if row[0] == id_[0]:
        table.remove(row)

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
    os.system("clear")
    record.insert(0, id_[0])
    for row in table:
        if row[0] == id_[0]:
            table[table.index(row)] = record[:]

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
    if the_same_longest_name:
        list_name_id = [the_same_longest_name, user_id_longest_name]
        for user_name, user_id in list_name_id[0] and list_name_id[0]:
            sort_name = ""
            sort_id = ""
            if user_name > sort_name:
                sort_name = user_name
                sort_id = user_id
                #the_same_longest_name.insert(0,user_name)
    return sort_id


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

    # your code
