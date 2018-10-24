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
    table = data_manager.get_table_from_file("model/hr/persons.csv")
    choice = None
    while choice != '0':
        choice = terminal_view.get_choice(options)
        if choice == '1':
            add()
        if choice == '2':
            remove()
        if choice == '3':
            update()
        if choice == '4':
            hr.get_oldest_person(table)
        if choice == '5':
            hr.get_persons_closest_to_average(table)

        else:
            terminal_view.print_error_message("There is no such choice.")


def add():
    table = data_manager.get_table_from_file("model/hr/persons.csv")
    record = terminal_view.get_inputs(["Name:", "Year:"], "Please provide following data:")
    hr.add(table, record)
    data_manager.write_table_to_file("model/hr/persons.csv", table)


def remove():
    table = data_manager.get_table_from_file("model/hr/persons.csv")
    id_ = terminal_view.get_inputs(["id_"], "Please provide ID you want to remove")
    hr.remove(table, id_)
    data_manager.write_table_to_file("model/hr/persons.csv", table)

def update():
    table = data_manager.get_table_from_file("model/hr/persons.csv")
    id_ = terminal_view.get_inputs(["id_"], "Please provide ID you want to edit")
    record = terminal_view.get_inputs(["Name:", "Year:"], "Please provide following data:")
    hr.update(table, id_, record)
    data_manager.write_table_to_file("model/hr/persons.csv", table)
