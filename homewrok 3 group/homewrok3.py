def concatenate_strings(str1: str, str2: str) -> str:
    """Функція конкатенує дві строки та повертає результат"""
    return str1 + str2


def count_list_elements(lst: list) -> int:
    """Функція підраховує кількість елементів у списку та повертає результат"""
    return len(lst)


if __name__ == '__main__':
    str1 = "Hello"
    str2 = "World"
    concatenated_str = concatenate_strings(str1, str2)
    print(concatenated_str)
    
    lst = [1, 2, 3, 4, 5]
    count_elements = count_list_elements(lst)
    print(count_elements)