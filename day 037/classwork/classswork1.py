def invert(lst):
    if lst == []:
        return []
    new_lst = []
    for i in lst:
        new_lst.append(i * -1)
    return new_lst
