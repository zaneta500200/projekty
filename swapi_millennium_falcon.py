#skrypt importuje z API pilotów Millennium Falcona i oblicza ich BMI

import requests
def isT(adres, nazwa):
    l = []
    resp=requests.get(adres)
    data=resp.json()
    nxt = data['next']
    sshp = data['results']
    for i in range(len(sshp)):
        l.append(sshp[i]['name'])
        tmp=sshp[i]
    if l.__contains__(nazwa) is not True:
        return isT(nxt, nazwa)
    else:
        tmp=sshp[l.index(nazwa)]
        return tmp
d=isT('https://swapi.co/api/starships/?page=1','Millennium Falcon')
peeps_url=d['pilots']

def BMI(m,h):
    m=int(m)
    h=int(h)
    bmi=m/(h/100)**2
    return bmi
plts={}
for i in peeps_url:
    resp=requests.get(i)
    data=resp.json()
    name=data['name']
    m=data['mass']
    h=data['height']
    bmi=BMI(m,h)
    tmp={name:bmi}
    plts.update(tmp)
print(plts)