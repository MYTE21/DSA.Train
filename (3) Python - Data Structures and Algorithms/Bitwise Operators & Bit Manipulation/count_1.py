def number_of_ones(binary):
    count = 0

    while binary:
        binary = binary & (binary - 1)
        count += 1

    return count


if __name__ == '__main__':
    print("10111: ", number_of_ones(0b10111))
