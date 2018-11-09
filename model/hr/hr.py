""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""




from model import data_manager
from model import common

# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """


    comparision_yr = 99999
    oldest_members = ['']
    for element in table:
        if int(element[2]) < comparision_yr:
            comparision_yr = int(element[2])
            oldest_members[0] = element[1]
        elif int(element[2]) == comparision_yr:
            oldest_members.append(element[1])
            
    return oldest_members



def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """
    sum = 0
    for element in table:
        sum += int(element[2])
    avg = sum / len(table)
     
    lowest_difference = 10000
    closest_members = ['']
    for element in table:
        if abs(int(element[2]) - avg) < lowest_difference:
            lowest_difference = abs(int(element[2]) - avg)
            closest_members[0] = element[1]
        elif int(element[2]) - avg == lowest_difference:
            closest_members.append(element[1])
        
    return closest_members


