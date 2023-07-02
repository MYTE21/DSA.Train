"""
Solution: Using nested-loops.
Time Complexity: O(n^2).
Space Complexity: O(max number of lists)
"""
from typing import List


def is_hotel_bookings_possible(arrive: List[int], depart: List[int], room: int):
    days = [0 for _ in range(max(arrive + depart) + 1)]

    for start, end in zip(arrive, depart):
        for i in range(start, end + 1):
            days[i] += 1
            if days[i] > room:
                return False

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
