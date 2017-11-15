#zwraca elementy zagnieżdżonej listy
inpt=[[[[[[[[['a'],'b']]],'c'],]],'d'],'e']

new=[]
def test(var):
    if type(var)is list:
        return True
    else:
        return False
def flatten(inpt):
    for i in inpt:
        if test(i) is True:
            flatten(i)
        else:
            new.append(i)
    return new
print(flatten(inpt))





