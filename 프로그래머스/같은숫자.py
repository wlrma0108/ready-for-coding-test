def solution(arr):
    if not arr:  # 1
        return []  # 2
    
    result = [arr[0]]  # 3
    for x in arr[1:]:  # 4
        if x != result[-1]:  # 5
            result.append(x)  # 6
    return result  # 7