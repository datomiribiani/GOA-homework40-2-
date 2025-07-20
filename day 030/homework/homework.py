# 1
def two_highest(arg1):
    c = []
    for i in arg1:
        if i == i:
            c.append(i)
    return c

# 2
def count_sheep(n):
    result = ""
    
    for i in range(1, n +1):
        result +=str(i) + " sheep..."
        
    return result

# 3
def reverse_seq(n):
    return list(range(n,0,-1))
