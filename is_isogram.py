def is_isogram(a):
    word=""
    a=a.lower()
    for i in range(len(a)):
        if a[i].isalpha():
            if a[i] in word:
                return False
                break
            else:
                word=word+a[i]
        else:
            word=word+a[i]        
    if word==a:
        return True

print(is_isogram("First# Clan!"))    
            
            