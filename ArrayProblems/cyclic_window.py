# Code implementation for cyclic_window.md problem


def shift_window(pixels: list, start_index: int, end_index: int, shift: int):
    for _ in range(shift):
        end = end_index - 1
        temp = pixels[end]
        while end != start_index:
            pixels[end] = pixels[end - 1]
            end -= 1
        pixels[start_index] = temp
    return pixels


def grid_shifter(pixels: list, partition_length: int, shift: int) -> list | None:
    if not pixels:
        return None

    shift = shift % partition_length
    if partition_length > len(pixels) or shift == 0:
        return pixels

    for start_index in range(0, len(pixels) - partition_length + 1, partition_length):
        end_index = start_index + partition_length
        shift_window(pixels, start_index, end_index, shift)

    return pixels
