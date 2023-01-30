def check_ith_bit_is_set(num, i):
    return True if num & (1 << i) else False


if __name__ == '__main__':
    print(check_ith_bit_is_set(20, 2))
