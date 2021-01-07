# not exactly like implode in PHP. PHP implode works with string
# this just IMPLODE
# turn [ [a1,a2,a3],[b1,b2,b3],[c1,c2,c3] ] into  [ a1,a2,a3,b1,b2,b3,c1,c2,c3 ]


def implode_function_from_php_bad_space_complexity(must_be_array):
    new_array = []
    for subarray in must_be_array:
        for element in subarray:
            new_array.append(element)
    return new_array


# 好题啊。。。
def implode_function_from_php_good_space_complexity(must_be_array):
    # 不会
    pass


def implode(must_be_array):
    if len(must_be_array) == 1:
        return must_be_array[0]
    else:
        new_array = []
        for subarray in must_be_array:
            for element in subarray:
                new_array.append(element)
        return new_array


# test
'''
test_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(
    implode_function_from_php_good_space_complexity(test_array)
)
'''
