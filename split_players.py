with open('euro_players_scrape.txt', 'r') as rf:
    euro_players=[]
    for line in rf:
        n=line.split('  ')
        euro_players.append(n[0])
with open('am_players_scrape.txt', 'r') as rf:
    am_players=[]
    for line in rf:
        n=line.split('  ')
        am_players.append(n[0])
print(am_players)