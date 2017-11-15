import requests
def isT(adres, nazwa):
    l = []
    resp=requests.get(adres)
    data=resp.json()
    nxt = data['next']
    gngn = data['results']
    for i in range(len(gngn)):
        l.append(gngn[i]['name'])
        tmp=gngn[i]
    if l.__contains__(nazwa) is not True:
        return isT(nxt, nazwa)
    else:
        tmp=gngn[l.index(nazwa)]
        return tmp
d=isT('https://swapi.co/api/species/','Gungan')
print(d)
peeps_url=d['people']
peeps=[]
for i in peeps_url:
    resp=requests.get(i+'?format=wookiee')
    data=resp.json()
    peeps.append(data['whrascwo'])
print(peeps)
