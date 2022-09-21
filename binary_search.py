def naive_search(l: list[int], target: int) -> int:
    for i, val in enumerate(l):
        if val == target:
            return i
    return -1


def bin_search(l: list[int], target: int) -> int:
    max = len(l) - 1
    min = 0

    while min <= max:
        mid = (min + max) // 2
        cur = l[mid]

        if cur == target:
            return mid

        if cur < target:
            min = mid + 1
        else:
            max = mid - 1

    return -1


from random import randint
from time import perf_counter


def main():
    length = 10_000
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))

    target = sorted_list[len(sorted_list) - 1]

    start1 = perf_counter()
    pos1 = naive_search(sorted_list, target)
    end1 = perf_counter()
    print(f"naive search took {end1-start1} seconds to return position {pos1}")

    builtin_start = perf_counter()
    builtin_pos = sorted_list.index(target)
    builtin_end = perf_counter()
    print(
        f"built-in list .index() method took {builtin_end-builtin_start} to return position {builtin_pos}"
    )

    start2 = perf_counter()
    pos2 = bin_search(sorted_list, target)
    end2 = perf_counter()
    print(f"binary search took {end2-start2} seconds to return position {pos2}")


if __name__ == "__main__":
    main()
