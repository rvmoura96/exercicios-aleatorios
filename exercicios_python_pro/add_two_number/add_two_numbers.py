def add_two_numbers(first_list_node: list, second_list_node: list) -> list:
    first_number = int(''.join(map(str, first_list_node)))
    second_number = int(''.join(map(str, second_list_node)))

    return_list = [int(x) for x in str(first_number + second_number)]

    return return_list
