def binary_search(list_of_sorted_data: list, item: int):
    """Binary search implementation for sorted data.
     Here we assume the item to be searched is an int."""
    start_index = 0
    stop_index = len(list_of_sorted_data) -1
    while stop_index <= stop_index:
        middle_index = (start_index + stop_index) // 2
        middle_value = list_of_sorted_data[middle_index]
        if middle_value > item:
            stop_index = middle_index - 1
        elif middle_value < item:
            start_index = middle_index + 1
        else:
            return middle_index
    return None


