def recNumCount(s):
    if s == '':
        return 0
    elif s[-1].isnumeric():
        return recNumCount(s[:-1])+1
        
    else:
        return(recNumCount(s[:-1]))
    pass
