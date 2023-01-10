""" InterviewBit
    Difficulty: Medium
    - Hotel Booking Possible
    - Problem Link: https://www.interviewbit.com/problems/hotel-bookings-possible/
"""


def is_hotel_bookings_possible(arrive, depart, room):
    events = [(arrival_day, 0) for arrival_day in arrive] + [(departure_day, 1) for departure_day in depart]
    events.sort()
    print(events)
    count = 0

    for event in events:
        if event[1] == 0:
            count += 1
        else:
            count -= 1
        if count > room:
            return False

    return True


if __name__ == "__main__":
    arrival_time = [1, 2, 3, 4]
    departure_time = [10, 2, 6, 14]
    total_room = 4

    print(is_hotel_bookings_possible(arrival_time, departure_time, total_room))