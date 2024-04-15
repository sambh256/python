def encrypt(letter,key):
    pot='abcdefghijklmnopqrstuvwxyz'
    k=len(letter)
    j=len(key)
    m=0
    e=""
    while j<k:
        key=key+key[m]
        m=(m+1)
        j=j+1
    for i in range (len(letter)):
        e=e+pot[(pot.index(key[i])+pot.index(letter[i]))%26]
        
    return e
def decrypt(letter,key):
    pot='abcdefghijklmnopqrstuvwxyz'
    k=len(letter)
    j=len(key)
    m=0
    d=""
    while j<k:
        key=key+key[m]
        m=(m+1)
        j=j+1
    for i in range (len(letter)):
        d=d+pot[(-(pot.index(key[i]))+pot.index(letter[i]))%26]
        
    return d
