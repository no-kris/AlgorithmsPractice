from ArrayProblems.cyclic_window import grid_shifter


def test_grid_shifter():
    # Example 1
    pixels1 = [1, 2, 3, 4, 5, 6, 7]
    p1, r1 = 3, 1
    expected1 = [3, 1, 2, 6, 4, 5, 7]
    assert grid_shifter(pixels1, p1, r1) == expected1, f"Failed Example 1: {pixels1}"

    # Example 2
    pixels2 = [1, 2, 3, 4, 5, 6, 7]
    p2, r2 = 2, 2
    expected2 = [1, 2, 3, 4, 5, 6, 7]
    assert grid_shifter(pixels2, p2, r2) == expected2, f"Failed Example 2: {pixels2}"

    # Example 3
    pixels3 = [1, 2, 3, 4, 5]
    p3, r3 = 5, 2
    expected3 = [4, 5, 1, 2, 3]
    assert grid_shifter(pixels3, p3, r3) == expected3, f"Failed Example 3: {pixels3}"

    # Edge Case: Small remaining window
    pixels4 = [1, 2, 3, 4, 5, 6]
    p4, r4 = 4, 1
    expected4 = [4, 1, 2, 3, 5, 6]
    assert grid_shifter(pixels4, p4, r4) == expected4, f"Failed Edge Case: {pixels4}"

    print("All tests passed!")


if __name__ == "__main__":
    test_grid_shifter()
