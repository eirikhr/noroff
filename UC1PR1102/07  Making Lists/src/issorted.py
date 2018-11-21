default_sorted_list = [1, 2, 3, 4, 5, 6, 7]
default_unsorted_list = [2, 1, 3, 4, 5, 6, 7]

def is_sorted(list):
    if sorted(list) == list:
        return True
    if sorted(list) != list:
        return False

print(is_sorted(default_unsorted_list))

