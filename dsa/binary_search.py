position = -1

def binary_search(thelist, search_value):
    lb = 0
    ub = len(thelist) - 1

    while lb <= ub:
        mid = (lb + ub) // 2

        if thelist[mid] == search_value:
            globals()['position'] = mid
            return True
        else:
            if search_value < thelist[mid]:
                ub = mid - 1
            else:
                lb = mid + 1
    return False


thelist = [2,8,11,19,20,25,36,44,55,66,77,88,99]
search_value = 36

if binary_search(thelist, search_value):
    print(f"Found the value {search_value} at position {position}")
else:
    print("Value not found")