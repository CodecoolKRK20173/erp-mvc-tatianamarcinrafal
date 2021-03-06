import model
from model import data_manager
from view import terminal_view
from model.hr import hr
from model import common       
import os   


def get_table_from(file):
    table = data_manager.get_table_from_file(file)
    return table


def save(file, table):
    data_manager.write_table_to_file(file, table)


def add(file, common_options):
    get_table_from(file)
    record = terminal_view.get_inputs([opt for opt in common_options], "Please provide following data: ")
    save(file, common.add(get_table_from(file), record)) 


def remove(file):
    get_table_from(file)
    id_ = terminal_view.get_input("ID: ", "Please provide ID, which you want to remove")
    save(file, common.remove(get_table_from(file), id_))
   

def update(file, common_options):
    get_table_from(file)
    id_ = terminal_view.get_input("ID: ", "Please provide ID, which you want to edit")
    record = terminal_view.get_inputs([opt for opt in common_options], "Please provide following data: ")
    save(file, common.update(get_table_from(file), id_, record))
    

def clear_instructions(file, title_list):
    os.system("clear")
    table = data_manager.get_table_from_file(file)
    terminal_view.print_table(table, title_list)

    return table
