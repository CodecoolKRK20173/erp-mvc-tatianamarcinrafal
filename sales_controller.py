# everything you'll need is imported:
from view import terminal_view

from model.sales import sales

from controller import common
from model import data_manager
import os


def run():
    options = ["Add", "Remove", "Update", "Lowest price item ID", "Items sold between", "Game title by ID", "All the Customer\'s IDs", "The sales of each customer", "The sales of each customer", "The number of sales of each customer", "The number of sales of each customer: "]
    common_options = ["Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
    link_for_csv = "model/sales/sales.csv"
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year", "Customer ID"]
    choice = None
    dont_clear = False
    while choice != '0':
        if not dont_clear:
            os.system("clear")
            table = data_manager.get_table_from_file(link_for_csv)
            terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice_submenu(options)
        dont_clear = False
        if choice == '1':
            common.add(link_for_csv, common_options)
        elif choice == '2':
            common.remove(link_for_csv)
        elif choice == '3':
            common.update(link_for_csv, common_options)
        elif choice == '4':
            lowest_price = sales.get_lowest_price_item_id(table)
            terminal_view.print_result(lowest_price, 'Lowest price game is: ')
            dont_clear = True
        elif choice == '5':
            dates_to_input = ['From month: ', 'From day: ', 'From year: ', 'To month:', 'To day: ', "To year: "]
            inputs = terminal_view.get_input(dates_to_input, "Please input appropriate data.")
            answer = sales.get_items_sold_between(table, int(inputs[0]), int(inputs[1]), int(inputs[2]), int(inputs[3]),
                                                  int(inputs[4]), int(inputs[5]))
            terminal_view.print_table(answer, title_list)
            dont_clear = True
        elif choice == '6':
            dates_to_input = 'Input ID: '
            inputs = terminal_view.get_input(dates_to_input, 'Please input appropriate data.')
            answer = sales.get_title_by_id(inputs)
            terminal_view.print_result(answer, 'Game title is: ')
            dont_clear = True
        elif choice == "7":
            terminal_view.print_result(sales.get_all_customer_ids_from_table(table), 'All the Customer\'s ID: ')
            dont_clear = True
        elif choice == "8":
            terminal_view.print_result(sales.get_all_sales_ids_for_customer_ids(), "The sales of each customer: ")
            dont_clear = True
        elif choice == "9":
            terminal_view.print_result(sales.get_all_sales_ids_for_customer_ids_form_table(table), "The sales of each customer: ")
            dont_clear = True
        elif choice == "10":
            terminal_view.print_result(sales.get_num_of_sales_per_customer_ids(), "The number of sales of each customer: ")
            dont_clear = True
        elif choice == "11":
            terminal_view.print_result(sales.get_num_of_sales_per_customer_ids_from_table(table), "The number of sales of each customer: ")
            dont_clear = True