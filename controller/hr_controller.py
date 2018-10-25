# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
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
    # os.system("clear")
    options = ["Add", "Remove", "Update", "Oldest person", "Persons closest to average"]
    common_options = ["Name: ", "Year: "]
    file = "model/hr/persons.csv"
    title_list = ["Id", "Name", "Year"]
    choice = None
    dont_clear = False
    while choice != '0':
        if not dont_clear:
            os.system("clear")
            table = data_manager.get_table_from_file(file)
            terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice_submenu(options)
        dont_clear = False
        if choice == '1':
            common.add(file, common_options)
        elif choice == '2':
            common.remove(file)
        elif choice == '3':
            common.update(file, common_options)
        elif choice == '4':
            terminal_view.print_result(hr.get_oldest_person(table))
            dont_clear = True
            # print here
        elif choice == '5':
            terminal_view.print_result(hr.get_persons_closest_to_average(table))
            dont_clear = True
            # print here
        else:
            terminal_view.print_error_message("There is no such choice.")

