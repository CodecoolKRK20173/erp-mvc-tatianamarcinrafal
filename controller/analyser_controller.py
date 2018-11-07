from view import terminal_view

from model.sales import sales

from controller import common
from model import data_manager
import os

# DONT WORK YET!


def run():
    options = ["Add", "Remove", "Update", "Lowest price item ID"]
    # common_options = ["Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
    # file = "model/sales/sales.csv"
    # title_list = ["ID", "Title", "Price", "Month", "Day", "Year", "Customer ID"]
    choice = None
    terminal_clear = False
    while choice != '0':
        if not terminal_clear:
            os.system("clear")
            table = common.clear_instructions(file, title_list)
        choice = terminal_view.get_choice_submenu(options)
        terminal_clear = False
        if choice == '1':
            common.add(file, common_options)
        elif choice == '2':
            common.remove(file)
        elif choice == '3':
            common.update(file, common_options)
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
