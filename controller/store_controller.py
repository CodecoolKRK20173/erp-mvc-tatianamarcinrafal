# everything you'll need is imported:
from view import terminal_view
from model.store import store
from controller import common
from model import data_manager


def run():
    options = ["Add", "Remove", "Update", "Count by manufacturer", "Average games in stock by manufacturer"]
    common_options = ["Title: ", "Manufacturer: ", "Price: ", "In stock: "]
    file = "model/store/games.csv"
    title_list = ["Id", "Title", "Manufacturer", "Price", "In stock"]
    choice = None
    terminal_clear = True
    while choice != '0':
        if terminal_clear:
            table = common.clear_instructions(file, title_list)
        choice = terminal_view.get_choice_submenu(options)
        terminal_clear = True
        if choice == '1':
            common.add(file, common_options)
        elif choice == '2':
            common.remove(file)
        elif choice == '3':
            common.update(file, common_options)
        elif choice == '4':
            msg = "Products by manufacturer:\n"
            terminal_view.print_result(store.get_counts_by_manufacturers(table), msg)
            terminal_clear = False
        elif choice == '5':
            manufacturer = terminal_view.get_inputs(["Manufacturer: "], "Please provide manufacturer name" )
            msg = "Average by " + manufacturer[0] + ":"
            value = store.get_average_by_manufacturer(table, manufacturer)
            terminal_view.print_result(value, msg)
            terminal_clear = False
        else:
            terminal_view.print_error_message("There is no such choice.")
