def nth_root(number,n):
    if n<0:
       raise ValueError("Negative roots can't be calculated")
    else:
        x = number**(1/n)
        return round(x,2)





