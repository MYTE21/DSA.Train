"""
Solution: Sorting the lists.
Time Complexity: O(n x log n).
Space Complexity: O(1)
"""
from typing import List


def is_hotel_bookings_possible(arrive: List[int], depart: List[int], room: int):
    arrive.sort()
    depart.sort()

    count = 0
    n = len(arrive)

    i, j = 0, 0
    while i < n and j < n:
        if arrive[i] <= depart[j]:
            count += 1
            if count > room:
                return False
            i += 1
        else:
            count -= 1
            j += 1

    return True


if __name__ == "__main__":
    arrivals_list = [
        [1, 3, 5],
        [1, 2, 3],
        [1, 2, 3]
    ]
    departures_list = [
        [2, 6, 8],
        [2, 3, 4],
        [2, 3, 4]
    ]
    room_count_list = [1, 2, 1]

    for arrivals, departures, rooms in zip(arrivals_list, departures_list, room_count_list):
        print(is_hotel_bookings_possible(arrivals, departures, rooms))
