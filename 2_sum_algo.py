

def two_sum_algo(array, sum):
    numbers = dict(enumerate(array))
    for i in numbers:
        num_for_check = sum - numbers[i]
        if num_for_check in numbers.values():
            return [numbers[i], num_for_check]
    return None

if __name__ == '__main__':
    array = [2, 8, 11, 1, 7]
    number = 15
    print(two_sum_algo(array, number))