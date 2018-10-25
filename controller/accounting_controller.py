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
    os.system("clear")
    title_list = ["ID", "Month", "Day", "Year", "Income or Outflow money", "Amount"]
    options = ["Add data", "Remove data", "Update data", "Year with the highest profit", "The average profit in a given year"]
    link_for_csv = 'model/accounting/items.csv'
    choice = None
    while choice != "0":
        table = data_manager.get_table_from_file(link_for_csv)    
        terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice_submenu(options)
        if choice == "1":
            add()
        elif choice == "2":
            remove()
        elif choice == "3":
            update()
        elif choice == "4":
            #table = data_manager.get_table_from_file(link_for_csv)            
            print(accounting.which_year_max(table))
        elif choice == "5":
            #table = data_manager.get_table_from_file(link_for_csv)
            year = input("Enter the year: ")
            print(accounting.avg_amount(table, year)
        else:
            terminal_view.print_error_message("There is no such choice.")

def add():
    link_for_csv = 'model/accounting/items.csv'
    table = data_manager.get_table_from_file(link_for_csv)
    title_list = ["Month: ", "Day: ", "Year: ", "Income (enter: 'in') or Outflow(enter:'out') money: ", "Amount: "]
    record = terminal_view.get_inputs(title_list, "Please provide following data:")
    accounting.add(table, record)
    data_manager.write_table_to_file(link_for_csv, table)

def remove():
    link_for_csv = 'model/accounting/items.csv'
    table = data_manager.get_table_from_file(link_for_csv)
    id_ = terminal_view.get_inputs(["ID: "], "Please provide ID you want to remove")
    accounting.remove(table, id_)
    data_manager.write_table_to_file(link_for_csv, table)

def update():
    link_for_csv = 'model/accounting/items.csv'
    table = data_manager.get_table_from_file(link_for_csv)
    id_ = terminal_view.get_inputs(["ID: "], "Please provide ID you want to edit")
    title_list = ["Month: ", "Day: ", "Year: ", "Income or Outflow money: ", "Amount: "]
    record = terminal_view.get_inputs(title_list, "Please provide following data:")
    accounting.update(table, id_, record)
    data_manager.write_table_to_file(link_for_csv, table)