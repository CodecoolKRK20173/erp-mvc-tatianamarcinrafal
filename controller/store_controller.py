# everything you'll need is imported:
from model.store import store
from view import terminal_view
from controller import common


def run():
    options = ["Add", "Remove", "Update", "Count by manufacturer[in progress]", "Average by manufacturer[in progress]"]
    common_options = ["Title: ", "Manufacturer: ", "Price: ", "In stock: "]
    file = "model/store/games.csv"
    table = common.get_table_from(file)
    choice = None
    while choice != '0':
        choice = terminal_view.get_choice(options)
        if choice == '1':
            common.add(file, common_options)
        if choice == '2':
            common.remove(file, common_options)
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
