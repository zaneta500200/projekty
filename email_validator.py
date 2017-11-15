def malpa(txt):
    try:
        w=txt.count('@')
        if w!=1:
            return False
        elif w==1 and txt.index('@')<1:
            return False
    except ValueError:
        return False
    else:
        return True
def kropka(txt):
    try:
        w= txt.rindex('.')
        if w!=(len(txt)-3) and w!=(len(txt)-4):
            return False
    except ValueError:
        return False
    else:
        return True
def kropka2(txt):
    cntr = []
    if txt.count('.')>1:
        for i in range(len(txt)):
            if txt[i]=='.':
                cntr.append(i)
    for i in range(len(cntr)):
        if cntr[i-1]==(cntr[i])-1:
            return False
    else:
        return True
def validator(txt):
    if malpa(txt) and kropka(txt) and txt.islower() and kropka2(txt):
        return True
    else:
        return False

print(validator('zl@@gd.com'))
