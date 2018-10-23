# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
import model
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
    terminal_view.get_choice(options)

    table = inventory.create_table()

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            add_item(table)
        elif choice == "2":
            hr_controller.run()
        elif choice == "3":
            inventory_controller.run()
        else:
            terminal_view.print_error_message("There is no such choice.")

def add_item(table):
    new_record = []
    new_record = terminal_view.get_inputs(['Name of item', 'Manufacturer', 'Year of purchase',
                                           'Years it can be used'], 'Please input information about platform: ')

    # table = inventory.create_file()
    new_record.insert(0, model.common.generate_random())
    ready_table = inventory.add(table, new_record)
    print(ready_table)

    # woła widok z inputami, po pobraniu inputow
    # To przesyla do model/inventory
