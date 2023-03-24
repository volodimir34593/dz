def sort_list(lst):
    return sorted(lst)
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sort_list(lst)
[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

lst = ['c', 'a', 'b', 'd']
sort_list(lst)
['a', 'b', 'c', 'd']
def filter_negatives(lst):
    return list(filter(lambda x: x < 0, lst))
lst = [-1, 2, -3, 4, -5, 6, 7, -8, 9, 10, -11]
filter_negatives(lst)
[-1, -3, -5, -8, -11]