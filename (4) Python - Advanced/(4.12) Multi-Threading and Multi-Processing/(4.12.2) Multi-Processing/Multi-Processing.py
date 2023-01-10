"""
    This `Multi-Processing.py` function is created instead of the `Multi-Processing.ipynb` file
    as multiprocessing module is not working properly in that file format. This thing needs to be
    investigated farther in the future.
"""
import multiprocessing
import time


def compute_fnc():
    print("inside compute_fnc")
    for x in range(10000000):
        _ = pow(x, 2)
    print("finished compute")


if __name__ == "__main__":
    t1 = time.perf_counter()

    process_list = [
        multiprocessing.Process(target=compute_fnc) for _ in range(5)
    ]

    for p in process_list:
        p.start()

    for p in process_list:
        p.join()

    t2 = time.perf_counter()
    time_spent = t2 - t1
    print(round(time_spent, 2))
    """ Output:
        inside compute_fnc
        inside compute_fnc
        inside compute_fnc
        inside compute_fnc
        inside compute_fnc
        finished compute
        finished compute
        finished compute
        finished compute
        finished compute
        4.67
    """