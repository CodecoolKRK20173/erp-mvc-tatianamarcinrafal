# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
from controller import common
from model import data_manager

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    title_list = ["ID", "Month", "Day", "Year", "Income(enter: 'in') or Outflow(enter:'out') money", "Amount"]
    options = ["Show table","Add data", "Remove data", "Update data"]
    link_for_csv = 'model/accounting/items.csv'
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            table = data_manager.get_table_from_file(link_for_csv)    
            terminal_view.print_table(table, title_list)
        elif choice == "2":
            add()
        elif choice == "3":
            remove()
        elif choice == "4":
            update()
        else:
            terminal_view.print_error_message("There is no such choice.")

def add():
    link_for_csv = 'model/accounting/items.csv'
    table = data_manager.get_table_from_file(link_for_csv)
    title_list = ["Month: ", "Day: ", "Year: ", "Income or Outflow money: ", "Amount: "]
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