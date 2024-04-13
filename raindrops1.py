def raindrop(num):
    a=""
    if num>0:
        if num%2==0:
            a=a+"rim jhim"
        if num%3==0:
            a=a+" jal tarang"
        if num%5==0:
            a=a+" baadal"
        if num%7==0:
            a=a+" chalte hai"
        if num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0:
            a=str(num)
    else:
        raise ValueError        
    return a.strip()
    
                        