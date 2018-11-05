# everything you'll need is imported:
from view import terminal_view
from model.store import store
from controller import common
from model import data_manager
import os


def run():
    options = ["Add", "Remove", "Update", "Count by manufacturer", "Average games in stock by manufacturer"]
    common_options = ["Title: ", "Manufacturer: ", "Price: ", "In stock: "]
    file = "model/store/games.csv"
    title_list = ["Id", "Title", "Manufacturer", "Price", "In stock"]
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
            msg = "Products by manufacturer:\n"
            terminal_view.print_result(store.get_counts_by_manufacturers(table), msg)
            dont_clear = True
        elif choice == '5':
            manufacturer = terminal_view.get_inputs(["Manufacturer: "], "Please provide manufacturer name" )
            msg = "Average by " + manufacturer[0] + ":"
            value = store.get_average_by_manufacturer(table, manufacturer)
            terminal_view.print_result(value, msg)
            dont_clear = True
        else:
            terminal_view.print_error_message("There is no such choice.")
