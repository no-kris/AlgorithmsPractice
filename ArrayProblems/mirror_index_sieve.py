# Implementation for the mirror_index_sieve.md problem in Python


def mirror_sieve(shelves: list) -> list:
    if not shelves:
        return []
    total_sum = sum(shelves)
    left_sum = 0
    indecis = []
    for index, item in enumerate(shelves):
        right_sum = total_sum - left_sum - item
        if left_sum == right_sum:
            indecis.append(index)
        left_sum += item
    return indecis
