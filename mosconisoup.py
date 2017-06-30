def makesoup(url):
    import requests, bs4, re
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    return(soup)
link = 'https://www.wikiwand.com/en/2016_Mosconi_Cup'
base = 'https://www.wikiwand.com/en/'
beg = '1998_Mosconi_Cup'
end = '2016_Mosconi_Cup'
tails=[]
for i in range(1998,2017):
    tails.append('{}_Mosconi_Cup'.format(i))
# soup = makesoup(link)
print(tails)