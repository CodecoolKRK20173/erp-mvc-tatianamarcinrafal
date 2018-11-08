# everything you'll need is imported:
from view import terminal_view

from model.sales import sales

from controller import common
from model import data_manager
import os


def run():
    options = ["Add", "Remove", "Update", "Lowest price item ID",
               "Items sold between", "Game title by ID", "All the Customer\'s IDs",
               "Item that was sold most recently", "The sales of each customer", 
               "The number of sales of each customer", "Sum of prices for given IDs",
               "Customer ID for Sale ID"]
    common_options = ["Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
    file = "model/sales/sales.csv"
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year", "Customer ID"]
    choice = None
    terminal_clear = False
    while choice != '0':
        if not terminal_clear:
            os.system("clear")
            table = common.clear_instructions(file, title_list)
        choice = terminal_view.get_choice_submenu(options)
        terminal_clear = False
        if choice == '1':
            sales.add(common_options)
        elif choice == '2':
            sales.remove()
        elif choice == '3':
            sales.update(common_options)
        elif choice == '4':
            lowest_price = sales.get_lowest_price_item_id(table)
            terminal_view.print_result(lowest_price, 'Lowest price game is: ')
            terminal_clear = True
        elif choice == '5':
            dates_to_input = ['From month: ', 'From day: ', 'From year: ', 'To month:', 'To day: ', "To year: "]
            inputs = terminal_view.get_input(dates_to_input, "Please input appropriate data.")
            answer = sales.get_items_sold_between(table, int(inputs[0]), int(inputs[1]), int(inputs[2]), int(inputs[3]),
                                                  int(inputs[4]), int(inputs[5]))
            terminal_view.print_table(answer, title_list)
            terminal_clear = True
        elif choice == '6':
            dates_to_input = 'Input ID: '
            inputs = terminal_view.get_input(dates_to_input, 'Please input appropriate Id.')
            answer = sales.get_title_by_id(inputs)
            terminal_view.print_result(answer+'\n', 'Game title is: \n')
            terminal_clear = True
        elif choice == "7":  # Tatiana
            terminal_view.print_result(sales.get_all_customer_ids_from_table(table), 'All the Customer\'s ID: ')
            terminal_clear = True
        elif choice == "8":
            terminal_view.print_result(sales.get_item_id_sold_last(), 'Item that was sold most recently')
            terminal_clear = True
        elif choice == "9":#Tatiana
            terminal_view.print_result(sales.get_all_sales_ids_for_customer_ids_form_table(table), "The sales of each customer: ")
            terminal_clear = True
        elif choice == "10":#Tatiana
            terminal_view.print_result(sales.get_num_of_sales_per_customer_ids_from_table(table), "The number of sales of each customer: ")
            terminal_clear = True    
        elif choice == "11":
            ids_amount = terminal_view.get_input("Amount of IDs: ", "How many IDs would you like to sum up?") 
            ids = []
            for i in range(int(ids_amount)):
                ids.append("Sale ID: ")
            inputs = terminal_view.get_inputs(ids, "Please provide an ID")
            result = sales.get_the_sum_of_prices_from_table(table, inputs)
            terminal_view.print_result(result, "Sum of prices for given IDs: ")
            terminal_clear = True
        elif choice == "12":
            sale_id = terminal_view.get_input("Sale ID: ", "Please provide sale ID")
            result = sales.get_customer_id_by_sale_id_from_table(table, sale_id)
            terminal_view.print_result(result, "Customer ID for Sale ID you provided: ")
            terminal_clear = True
        else:
            terminal_view.print_error_message("There is no such choice, please try again")

def input_for_add_menu():
    '''

    This function exists because test.py reads terminal_view.get_input()
    as usage of standard input() function. What can you do?

    '''
    return terminal_view.get_input("Crm ID: ", "Please provide existing user ID")