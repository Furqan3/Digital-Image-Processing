def min_max_normalization(lst):
    
    min_val = min(lst)
    max_val = max(lst)
    if min_val == max_val:
        return [0] * len(lst)
    normalized_lst = []
    for x in lst:
        normalized_x = (x - min_val) / (max_val - min_val)
        normalized_lst.append(normalized_x)
    return normalized_lst
mylist=[5,8,0,45,7,3,9,2,90]
print(min_max_normalization(mylist))