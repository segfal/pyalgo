


def add_digits(num):
    if num < 10:
        return num
    else:
        return add_digits(sum([int(i) for i in str(num)]))
    
def add_digits2(num):
    if num < 10:
        return num
    else:
        return add_digits2(num % 10 + num // 10)

