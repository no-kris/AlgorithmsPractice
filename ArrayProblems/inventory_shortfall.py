# Implementation for inventory_shortfall.md problem.


def find_smallest_missing_id(products: list) -> int:
    if not products:
        return 0

    expected_id = 0
    for id in products:
        if id != expected_id:
            return expected_id
        expected_id += 1
    return expected_id
