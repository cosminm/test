def find_index_non_optimized(input_list):
    if input_list is None or type(input_list) is not list:
        return []
    result = []
    dim = len(input_list)

    [result.append(i-1)
     for i in range(dim)
     if sum(input_list[:i]) == sum(input_list[i:])
     ]
    return result


def find_index_optimized(input_list):
    if input_list is None or type(input_list) is not list:
        return []
    result = []
    dim = len(input_list)
    s1 = 0
    s2 = sum(input_list)

    for i in range(dim):
        s1 += input_list[i]
        s2 -= input_list[i]
        if s1 == s2:
            result.append(i)
    return result

