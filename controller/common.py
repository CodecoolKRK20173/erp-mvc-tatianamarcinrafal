import model
from model import data_manager
from view import terminal_view
from model.hr import hr              #pomocy za dużo importów


def get_table_from(file):
    table = data_manager.get_table_from_file("model/hr/persons.csv")
    return table


def save(file, table):
    data_manager.write_table_to_file(file, table)

def add(file):
    get_table_from(file)
    record = terminal_view.get_inputs(["Name:", "Year:"], "Please provide following data:")
    save(file, hr.add(get_table_from(file), record))
    # print here


def remove(file):
    get_table_from(file)
    id_ = terminal_view.get_inputs(["id_"], "Please provide ID you want to remove")
    save(file, hr.remove(get_table_from(file), id_))
    # print here

def update(file):
    get_table_from(file)
    id_ = terminal_view.get_inputs(["id_"], "Please provide ID you want to edit")
    record = terminal_view.get_inputs(["Name:", "Year:"], "Please provide following data:")
    save(file, hr.update(get_table_from(file), id_, record))
    # print here
