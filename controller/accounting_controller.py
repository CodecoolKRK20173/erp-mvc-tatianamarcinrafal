# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
from controller import common
from model import data_manager
import os
from time import sleep

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    options = ["Add data", "Remove data", "Update data", "Year with the highest profit", "The average profit for a given year"]
    common_options = ["Month: ", "Day: ", "Year: ", "Income (enter: 'in') or Outflow(enter:'out') money: ", "Amount: "]
    link_for_csv = 'model/accounting/items.csv'
    title_list = ["ID", "Month", "Day", "Year", "Income or Outflow money", "Amount"]
    choice = None
    dont_clear = False
    while choice != "0":
        if not dont_clear:
            os.system("clear")
            table = data_manager.get_table_from_file(link_for_csv)
            terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice_submenu(options)
        dont_clear = False
        if choice == "1":
            common.add(link_for_csv, common_options)
        elif choice == "2":
            common.remove(link_for_csv)
        elif choice == "3":
            common.update(link_for_csv, common_options)
        elif choice == "4":
            terminal_view.print_result(accounting.which_year_max(table), "Year with the highest profit: ")
            dont_clear = True
        elif choice == "5":
            year = int(terminal_view.get_input("Year: ", "Enter a year to find out an average profit: "))
            terminal_view.print_result(accounting.avg_amount(table, year), 'The average profit for a given year: ')
            dont_clear = True
        else:
            terminal_view.print_error_message("There is no such choice, please try again")