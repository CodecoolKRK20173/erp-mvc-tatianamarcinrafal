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
    os.system("clear")
    options = ["Add", "Remove", "Update", "Oldest person", "Persons closest to average"]
    common_options = ["Name: ", "Year: "]
    file = "model/hr/persons.csv"
    table = data_manager.get_table_from_file(file)
    choice = None
    title_list = ["Id", "Name", "Year"]
    while choice != '0':
        terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice_submenu(options)
        if choice == '1':
            common.add(file, common_options)
        if choice == '2':
            common.remove(file)
        if choice == '3':
            common.update(file, common_options)
        if choice == '4':
            hr.get_oldest_person(table)
            # print here
        if choice == '5':
            hr.get_persons_closest_to_average(table)
            # print here

        else:
            terminal_view.print_error_message("There is no such choice.")

