def plus_one(digits):
    if digits[-1] != 9:
        digits[-1] += 1
        return digits
    else:
        if len(digits) == 1:
            return [1, 0]
        else:
            digits[-1] = 0
            digits[:-1] = plus_one(digits[:-1])
            return digits

