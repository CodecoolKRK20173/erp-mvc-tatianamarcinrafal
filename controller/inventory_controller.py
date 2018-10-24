# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
import model
from model import data_manager
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    options = ['Add item', 'Edit item', 'Remove item']
    # terminal_view.get_choice(options)
    link_to_csv = 'model/inventory/inventory.csv'
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice_submenu(options)
        if choice == "1":
            add_item(link_to_csv)
        elif choice == "2":
            edit_item(link_to_csv)
        elif choice == "3":
            inventory_controller.run()
        else:
            terminal_view.print_error_message("There is no such choice.")


def add_item(link_to_csv):
    # new_record = []
    column_names = ['Id', 'Name of item', 'Manufacturer', 'Year of purchase',
                                           'Used years']
    new_record = terminal_view.get_inputs(['Name of item: ', 'Manufacturer: ', 'Year of purchase: ',
                                           'Years it can be used: '], 'Please input information about platform: ')

    table = data_manager.get_table_from_file(link_to_csv)
    new_record.insert(0, model.common.generate_random(table))
    ready_table = inventory.add(table, new_record)
    data_manager.write_table_to_file(link_to_csv, ready_table)
    
    terminal_view.print_table(ready_table, column_names)

def edit_item(link_to_csv):
    table = data_manager.get_table_from_file(link_to_csv)
    # print(table)
    what_id_edit = terminal_view.get_inputs(["Ids' number: "], 'What position (by id) do you want edit: ')
    
    for record in table:
        if str(record[0]) == what_id_edit[0]:
            terminal_view.print_result(record, '') #drukuje liste
        