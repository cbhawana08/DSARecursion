def sum_d(n):
    if n>0:
        return((n%10)+sum_d(n//10))
    else:
        return(0)
print(sum_d(32))
print(sum_d(32342))
