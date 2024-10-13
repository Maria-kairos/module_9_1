def apply_all_func(int_list, *functions):
    results = {}
    for f in functions:
        results[f.__name__] = f(int_list)
    return results

def min_arg(int_list):
    return min(int_list)

def max_arg(int_list):
    return max(int_list)

def len_arg(int_list):
    return len(int_list)

def sum_arg(int_list):
    return sum(int_list)

def sorted_arg(int_list):
    return sorted(int_list)

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

