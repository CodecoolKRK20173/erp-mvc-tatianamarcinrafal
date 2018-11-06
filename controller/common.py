import model
from model import data_manager
from view import terminal_view
from model.hr import hr
from model import common             


def get_table_from(file):
    table = data_manager.get_table_from_file(file)
    return table


def save(file, table):
    data_manager.write_table_to_file(file, table)

# file - path to file you work on, defined in <section>_controller.py
# common_options - list of strings being names of entry options, also defined in <section>_controller.py

def add(file, common_options):
    get_table_from(file)
    record = terminal_view.get_inputs([opt for opt in common_options], "Please provide following data: ")
    save(file, common.add(get_table_from(file), record)) 
    # print here


def remove(file):
    get_table_from(file)
    id_ = terminal_view.get_input("ID: ", "Please provide ID, which you want to remove")
    save(file, common.remove(get_table_from(file), id_))
    # print here

def update(file, common_options):
    get_table_from(file)
    id_ = terminal_view.get_input("ID: ", "Please provide ID, which you want to edit")
    record = terminal_view.get_inputs([opt for opt in common_options], "Please provide following data: ")
    save(file, common.update(get_table_from(file), id_, record))
    # print here
