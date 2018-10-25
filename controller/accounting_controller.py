# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
from controller import common
from model import data_manager
import os

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    options = ["Add data", "Remove data", "Update data", "Year with the highest profit", "The average profit in a given year"]
    common_options = ["Month: ", "Day: ", "Year: ", "Income (enter: 'in') or Outflow(enter:'out') money: ", "Amount: "]
    link_for_csv = 'model/accounting/items.csv'
    title_list = ["ID", "Month", "Day", "Year", "Income or Outflow money", "Amount"]
    choice = None
    while choice != "0":
        os.system("clear")
        table = data_manager.get_table_from_file(link_for_csv)
        terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice_submenu(options)
        if choice == "1":
            common.add(link_for_csv, common_options)
        elif choice == "2":
            common.remove(link_for_csv)
        elif choice == "3":
            common.update(link_for_csv, common_options)
        elif choice == "4":
            #table = data_manager.get_table_from_file(link_for_csv)            
            print(accounting.which_year_max(table))
        elif choice == "5":
            #table = data_manager.get_table_from_file(link_for_csv)
            year = input("Enter the year: ")
            #print(accounting.avg_amount(table, year))
        else:
            terminal_view.print_error_message("There is no such choice.")