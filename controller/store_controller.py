# everything you'll need is imported:
from model.store import store
from view import terminal_view
from controller import common
from model import data_manager
import os


def run():
    os.system("clear")
    options = ["Add", "Remove", "Update", "Count by manufacturer[in progress]", "Average by manufacturer[in progress]"]
    common_options = ["Title: ", "Manufacturer: ", "Price: ", "In stock: "]
    file = "model/store/games.csv"
    title_list = ["Id", "Title", "Manufacturer", "Price", "In stock"]
    choice = None
    while choice != '0':
        os.system("clear")
        table = data_manager.get_table_from_file(file)
        terminal_view.print_table(table, title_list)
        choice = terminal_view.get_choice_submenu(options)
        if choice == '1':
            common.add(file, common_options)
        if choice == '2':
            common.remove(file)
        if choice == '3':
            common.update(file, common_options)
        if choice == '4':
            store.get_counts_by_manufacturers
            # print here
        if choice == '5':
            store.get_average_by_manufacturer
            # print here

        else:
            terminal_view.print_error_message("There is no such choice.")
