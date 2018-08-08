def itemCount(lst):
    if lst == []:
        return 0
    elif type(lst[-1]) == list:
        return itemCount(lst[-1])
    else:
        return itemCount(lst[:-1]) + 1
