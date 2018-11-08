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
    # your code

#Tatiana
def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """
    link_for_csv_sales = "model/sales/sales.csv"
    table_sales = data_manager.get_table_from_file(link_for_csv_sales)
    link_for_csv_customers = "model/crm/customers.csv"
    table_customers = data_manager.get_table_from_file(link_for_csv_customers)    
    customer_money = {}
    game_prices = 0
    customer = ''
    
    for row in table_sales:
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
    answer = []
    if customer_max_value:
        id_customer = customer_max_value[0]
        spent_money = customer_max_value[1]
        for row in table_customers:
            id_customer_table = row[0]
            name_customer = row[1]
            if id_customer_table == id_customer:
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

    link_for_csv_sales = "model/sales/sales.csv"
    table_sales = data_manager.get_table_from_file(link_for_csv_sales)
    link_for_csv_customers = "model/crm/customers.csv"
    table_customers = data_manager.get_table_from_file(link_for_csv_customers)    
    customer_money = {}
    game_prices = 0
    customer = ''
    
    for row in table_sales:
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
get_the_buyer_id_spent_most_and_the_money_spent()

def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """

    # sales_table = common.get_table_from("model/sales/sales.csv")
    # customers_table = common.get_table_from("model/crm/customers.csv")
    # most_frq_buyr = 0
    # for iterations in range(num):
    #     for element in sales_table:
    #         if element[3] > most_frq_buyr:
    #             most_frq_buyr = element[3] 
            


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """

    # your code
