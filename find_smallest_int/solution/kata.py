def find_smallest_int(arr: list[int]) -> int:
    smallest = None
    for number in arr:
        if smallest is None:
            smallest = number
        elif number < smallest:
            smallest = number
    return smallest
