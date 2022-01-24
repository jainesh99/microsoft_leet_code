def generalizedGCD(num, arr):
    # max_value = max(arr)
    # gcd = 1
    #
    # for i in range(2, max_value+1):
    #     counter = 0
    #
    #     for value in arr:
    #
    #         if (value >= 0) and (value % i == 0):
    #             counter += 1
    #
    #     if counter == num:
    #         gcd = i
    #
    # return gcd

    def gcd(a, b):

        while b > 0:
            a, b = b, a % b
        return a

    result = arr[0]

    for i in arr[1:]:
        result = gcd(result, i)

    return result


print(generalizedGCD(2, [0, 18]))
