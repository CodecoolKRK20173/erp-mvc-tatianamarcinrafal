"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoud using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
from view import terminal_view
from model import common
from model.sales import sales
from model.crm import crm
from controller import common
from model import data_manager


#global variables, don't change them
sales_table = common.get_table_from("model/sales/sales.csv")
customers_table = common.get_table_from("model/crm/customers.csv")


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code

    pass


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """

    # id from sales_controller get_item_id_sold_last
    game_id_sold_last = sales.get_item_id_sold_last()

    customer_id  = sales.get_customer_id_by_sale_id(game_id_sold_last)

    return crm.get_name_by_id(customer_id)


    
def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """

    game_id_sold_last = sales.get_item_id_sold_last()

    customer_id  = sales.get_customer_id_by_sale_id(game_id_sold_last)

    return customer_id


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """
    customer_max_value = get_the_buyer_id_spent_most_and_the_money_spent()
    id_customer = customer_max_value[0]
    answer = []
    if customer_max_value:
        id_customer = customer_max_value[0]
        spent_money = customer_max_value[1]
        name_customer = crm.get_name_by_id_from_table(customers_table, id_customer)    
        answer.append(name_customer)
        answer.append(spent_money)
    name_answer = tuple(answer)
    return name_answer




def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """
    customer_money = {}
    game_prices = 0
    customer = ''
    
    for row in sales_table:#sales_table is a global variable
        money = int(row[2])
        customer = row[6]
        if customer not in customer_money.keys():
            customer_money[customer] = money
        else:
            customer_money[customer] += money
    
    max_value = 0
    customer_max_value = []
    if customer_money:
        for key, value in customer_money.items():
            if value > max_value:
                max_value = value
                if customer_max_value:
                    customer_max_value[0] = key
                    customer_max_value[1] = max_value
                else:
                    customer_max_value.append(key)
                    customer_max_value.append(max_value)
    customer_max_value = tuple(customer_max_value)

    return customer_max_value

def get_the_most_frequent_buyers_names(num):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """
    full_list_of_buyers = get_the_most_frequent_buyers_ids(num)
    full_list_of_buyers_by_name = []
    for element in full_list_of_buyers:
        for csv_element in customers_table:
            if element[0] == csv_element[0]:
                full_list_of_buyers_by_name.append((csv_element[1], element[1]))

    return full_list_of_buyers_by_name


def get_the_most_frequent_buyers_ids(num):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """
    def scan_list_of_buyers(lis, id_):
        for element in lis:
            if id_ == element[0]:
                return False
        return True

    full_list_of_buyers = []
    most_frq_buyr = 0
    for iterations in range(num):
        for element in sales_table:
            if int(element[2]) > most_frq_buyr and scan_list_of_buyers(full_list_of_buyers, element[6]):
                    most_frq_buyr = int(element[2])
        for element in sales_table:
            if int(element[2]) == most_frq_buyr:
                full_list_of_buyers.append((element[6], element[2]))
                most_frq_buyr = 0
    return full_list_of_buyers
