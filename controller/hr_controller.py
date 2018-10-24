# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
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
    options = ["Add", "Remove", "Update", "Oldest person", "Persons closest to average"]
    file = "model/hr/persons.csv"
    table = common.get_table_from(file)
    choice = None
    while choice != '0':
        choice = terminal_view.get_choice(options)
        if choice == '1':
            common.add(file)
        if choice == '2':
            common.remove(file)
        if choice == '3':
            common.update(file)
        if choice == '4':
            hr.get_oldest_person(table)
            # print here
        if choice == '5':
            hr.get_persons_closest_to_average(table)
            # print here

        else:
            terminal_view.print_error_message("There is no such choice.")

