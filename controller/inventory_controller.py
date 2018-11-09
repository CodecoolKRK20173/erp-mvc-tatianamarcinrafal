# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
import model
from model import data_manager
from controller import common
import os

labels = ['Id', 'Name of item', 'Manufacturer', 'Year of purchase',
          'Used years']
table = data_manager.get_table_from_file('model/inventory/inventory.csv')


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    options = ['Add item', 'Edit item', 'Remove item', 'Which items have not exceeded their durability yet',
               'What are the average durability times for each manufacturer']
    link_to_csv = 'model/inventory/inventory.csv'
    common_options = ['Name of item: ', 'Manufacturer: ', 'Year of purchase: ',
                      'Years it can be used: ']
    title_list = ["Id", "Name", "Manufacturer", "Year of purchase", "Years it can be used"]
    choice = None
    dont_clear = False
    while choice != "0":
        if not dont_clear:
            os.system("clear")
            table = data_manager.get_table_from_file(link_to_csv)
            terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice_submenu(options)
        dont_clear = False
        if choice == "1":
            common.add(link_to_csv, common_options)
        elif choice == "2":
            common.update(link_to_csv, common_options)
        elif choice == "3":
            common.remove(link_to_csv)
        elif choice == "4":
            os.system("clear")
            table_to_print = inventory.get_available_items(table)
            terminal_view.print_table(table_to_print, labels)
            
            dont_clear = True
        elif choice == "5":
            terminal_view.print_result(inventory.get_average_durability_by_manufacturers(
                table), '\nWhat are the average durability times for each manufacturer: ')
            dont_clear = True
        else:
            terminal_view.print_error_message("There is no such choice.")


def add_item(link_to_csv, labels):

    new_record = terminal_view.get_inputs(['Name of item: ', 'Manufacturer: ', 'Year of purchase: ',
                                           'Years it can be used: '], 'Please input information about platform: ')

    table = data_manager.get_table_from_file(link_to_csv)
    new_record.insert(0, model.common.generate_random(table))
    ready_table = inventory.add(table, new_record)
    data_manager.write_table_to_file(link_to_csv, ready_table)

    terminal_view.print_table(ready_table, labels)


def update_item(link_to_csv, labels):
    table = data_manager.get_table_from_file(link_to_csv)

    terminal_view.print_table(table, labels)
    what_id_edit = terminal_view.get_inputs(["Ids' number: "], 'What position (by id) do you want edit: ')

    for record in table:
        if str(record[0]) == what_id_edit[0]:
            terminal_view.print_result(record, '')  
