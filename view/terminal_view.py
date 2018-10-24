""" Terminal view module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    table.insert(0, title_list)
    table_with_titles = table
    how_many_column = len(title_list)
    the_logest_item_in_each_column = []
    empty_list = True
    for item in table_with_titles:
        for index, value in enumerate(item):
            if empty_list:
                the_logest_item_in_each_column.append(len(value))
            else:
                if the_logest_item_in_each_column[index] < len(value):
                    the_logest_item_in_each_column[index] = len(value)
        empty_list = False

    sum_of_all_characters = 0
    for item in the_logest_item_in_each_column:
        sum_of_all_characters += item

    how_much_free_space_around_word = 3
    width_table = sum_of_all_characters + (how_much_free_space_around_word*2*how_many_column)-1
    line = 0
    print('\n' + '-'*width_table)
    for row in table_with_titles:
        for i in range(how_many_column):
            a = the_logest_item_in_each_column[i]+how_much_free_space_around_word
            print(row[i].center(a, ' '), end=' | ')
        print('\n' + '-'*width_table)


def print_result(result, label=''):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    if type(result) == str:
        if label:
            print(f'{label}')
        print(f'{result}')
    elif type(result) == list:
        if label:
            print(label)
        for item in result:
            print(item)
    elif type(result) == dict:
        if label:
            print(label)
        for key, value in result.items():
            print(f'{key} -> {value}')


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code

    print(f'{title}')
    for numb, options in enumerate(list_options, 1):
        numb = f'({numb})'
        print(f'{numb:>6} {options}')
    zero_option = '(0)'
    print(f'{zero_option:>6} {exit_message}')


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    if title:
        print(f'{title}')
    inputs = []
    for labels in list_labels:
        inputs.append(input(labels))

    return inputs


def get_choice(options):
    print_menu("Main menu", options, "Exit program")
    inputs = get_inputs(["Please enter a number: "], "")
    return inputs[0]


def get_choice_submenu(options):
    print_menu("Submenu", options, "Exit program")
    inputs = get_inputs(["Please enter a number: "], "")
    return inputs[0]


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def main():
    dictio = {'key': 'value_1',
              'key_2': 'value2'}

    print_result(dict(dictio), 'label')


if __name__ == '__main__':
    main()
