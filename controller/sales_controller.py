# everything you'll need is imported:
from view import terminal_view
from model.sales import sales
from controller import common
from model import data_manager
import os


def run():
    options = ["Add", "Remove", "Update", "Lowest price item ID", "Items sold between", "Game title by ID"]
    common_options = ["Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
    file = "model/sales/sales.csv"
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year", "Customer ID"]
    choice = None
    dont_clear = False
    options_which_no_table_show = ['4', '5', '6']
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
            common.add(file, common_options)
        if choice == '2':
            common.remove(file)
        if choice == '3':
            common.update(file, common_options)
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
        if choice == '6':
            # os.system("clear")
            dates_to_input = 'Input ID: '
            inputs = terminal_view.get_input(dates_to_input, 'Please input appropriate data.')
            answer = sales.get_title_by_id(inputs)
            terminal_view.print_result(answer, 'Game title is: ')
            dont_clear = True
