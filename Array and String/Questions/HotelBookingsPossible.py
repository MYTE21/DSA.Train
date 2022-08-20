"""
    InterviewBit
    - Hotel Booking Possible
    - Problem Link: https://www.interviewbit.com/problems/hotel-bookings-possible/
"""


def is_hotel_bookings_possible(arrive, depart, room):
    arrive.sort(), depart.sort()
    len_a, len_d = 0, 0
    count = 0
    n = len(arrive)

    while len_a < n and len_d < n:
        if arrive[len_a] <= depart[len_d]:
            count += 1
            if count > room:
                return False
            len_a += 1
        else:
            count -= 1
            len_d += 1

    return True


if __name__ == "__main__":
    arrival_time = [1, 2, 3, 4]
    departure_time = [10, 2, 6, 14]
    total_room = 4

    print(is_hotel_bookings_possible(arrival_time, departure_time, total_room))