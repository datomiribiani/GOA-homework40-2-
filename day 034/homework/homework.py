# 3
def square_sum(numbers):
    squar_sum = 0
    for i in numbers:
        squar_sum += i*i
    return squar_sum

# 4
def kata_13_december(lst): 
    for i in range(len(lst)): 
        if lst[i]%2==0: 
            lst.remove(i)
    return lst
