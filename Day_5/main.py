def unsorted_search(list_of_unsorted_data: list, item: int):
    """linear search implementation for non-sorted data.
     Here we assume the item to be searched is an int."""
    for index in range(len(list_of_unsorted_data)):
        if list_of_unsorted_data[index] == item:
            return index
    return None



def sorted_search(list_of_sorted_data: list, item: int):
    """linear search implementation for sorted data.
     Here we assume the item to be searched is an int."""
    for index in range(len(list_of_sorted_data)):
        if list_of_sorted_data[index] == item:
            return index
        elif list_of_sorted_data[index] > item:
            return None
    return None

