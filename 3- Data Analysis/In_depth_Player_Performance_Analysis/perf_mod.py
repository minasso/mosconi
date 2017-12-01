def setup_df(player, team):
    import pickle
    import pandas as pd
    path = '//DREW/Users/andrew/Desktop/mosconi/'
    dframe = pickle.load(open(path+'pkl/allyears_clean_locs','rb'))
    dframe['Europe_lost'] = ~ dframe['Europe_won']
    if 'a' in team.lower():
        df = dframe[dframe['American_player'].str.contains(player)]
        df = df[['Format', 'European_player', 'European_score', 'American_score',
           'American_player', 'Europe_lost','Europe_won']]
        df.columns = ['Format', 'European_player', 'European_score', 'American_score',
           'American_player', 'America_won', 'America_lost']
    else:
        df = dframe[dframe['European_player'].str.contains(player)]
    return(df,dframe)

def stats(df,team):
    try:
        if 'a' in team.lower():
            win = df['America_won'].sum()
            loss = df['America_lost'].sum()
        else:
            win = df['Europe_won'].sum()
            loss = df['Europe_lost'].sum()
        mp= win+loss
        wl = 'Win-loss: {}-{}'.format(win,loss)
        pct = round(win/(win+loss)*100,0)
        return('Matches Played: {}'.format(mp),wl,'Pct: {}'.format(pct))
    except:
        return('No matches to display')

def overall_stats(df,team):
    sing = df[df['Format']=='Singles']
    dub = df[df['Format']=='Doubles']
    teams = df[df['Format']=='Teams']
    triples = df[df['Format']=='Triples'] 
    outstr='Overall: {}\nSingles: {}\nDoubles: {}\nTeams:   {}\nTriples: {}\n'.format(stats(df,team), stats(sing,team), stats(dub,team), stats(teams,team), stats(triples,team))
    print(outstr)
    return(sing,dub,teams,triples)

def overall_stats_2(df,team):
    sing = df[df['Format']=='Singles']
    dub = df[df['Format']=='Doubles']
    teams = df[df['Format']=='Teams']
    triples = df[df['Format']=='Triples'] 
    outstr='Overall: {}\nSingles: {}\nDoubles: {}\nTeams:   {}\nTriples: {}\n'.format(stats(df,team), stats(sing,team), stats(dub,team), stats(teams,team), stats(triples,team))
    # print(outstr)
    return(sing,dub,teams,triples)

def partners(dub,player):
    if 'America_won' in dub:
        dub = dub[['European_player','American_player','America_won','America_lost']].copy()
        dub['Partner']=dub['American_player'].str.replace(player,'')
        dub['Partner']=dub['Partner'].str.replace('&','')
        dub['Partner']=dub['Partner'].str.strip()
        d = dub.groupby('Partner').sum().sort_values(['America_won','America_lost'],ascending=False)
        return d    
    else:
        dub = dub[['European_player','American_player','Europe_won','Europe_lost']]
        dub['Partner']=dub['European_player'].str.replace(player,'')
        dub['Partner']=dub['Partner'].str.replace('&','')
        dub['Partner']=dub['Partner'].str.strip()
        return dub.groupby('Partner').sum().sort_values(['Europe_won','Europe_lost'],ascending=False)

def partners_2(dub,player):
    if 'America_won' in dub:
        dub = dub[['European_player','American_player','America_won','America_lost']].copy()
        dub['Partner']=dub['American_player'].str.replace(player,'')
        dub['Partner']=dub['Partner'].str.replace('&','')
        dub['Partner']=dub['Partner'].str.strip()
        return dub.groupby('Partner').sum().sort_values(['America_won','America_lost'],ascending=False).nlargest(1,columns='America_won')   
    else:
        dub = dub[['European_player','American_player','Europe_won','Europe_lost']]
        dub['Partner']=dub['European_player'].str.replace(player,'')
        dub['Partner']=dub['Partner'].str.replace('&','')
        dub['Partner']=dub['Partner'].str.strip()
        return dub.groupby('Partner').sum().sort_values(['Europe_won','Europe_lost'],ascending=False).nlargest(1,columns='Europe_won')

def opponents(sing):
    if 'America_won' in sing:
        return sing.groupby('European_player').sum().sort_values('America_won',ascending = False)
    else:
        return sing.groupby('American_player').sum().sort_values('Europe_won',ascending = False)

def opponents_2(sing):
    if 'America_won' in sing:
        return sing.groupby('European_player').sum().sort_values('America_won',ascending = False).nlargest(1,columns='America_won')
    else:
        return sing.groupby('American_player').sum().sort_values('Europe_won',ascending = False).nlargest(1,columns='Europe_won')

def yearly_plot(df):
    import numpy as np
    import matplotlib.pyplot as plt
    lst =df.index.values.tolist() 
    years = set([])
    for item in lst:
        years.add(item[0])
    years=list(years)

    yearly=[]
    for year in years:
        if 'America_won' in df:
            w = df.loc[year]['America_won'].sum()
            l = df.loc[year]['America_lost'].sum()
        else:
            w = df.loc[year]['Europe_won'].sum()
            l = df.loc[year]['Europe_lost'].sum()
        yearly.append((w,l))

    yr= {}
    for k,v in zip(years,yearly):
        yr[k]=v

    win=[]
    loss=[]
    pct=[]
    for w,l in yearly:
        win.append(w)
        loss.append(l)
        p=round((w*100/(w+l)),0)
        pct.append(p)

    # from IPython.core.interactiveshell import InteractiveShell
    # InteractiveShell.ast_node_interactivity = "last_expr"

    fig = plt.figure(figsize=(14, 8))
    ax = fig.add_subplot(111)

    x= years
    y= pct

    ind = range(len(years))  

    ax.plot(y,linestyle='-',marker='.',markersize=12)
    ax.axhline(50, color='r',linestyle='--')

    ax.set_ylabel('Percentage of Games Won');
    ax.set_title('Yearly Performance Average');
    ax.set_xticks(ind);
    ax.set_xticklabels(x,rotation=30);

    for i in range(len(years)):
        plt.annotate( '{}-{}'.format(yearly[i][0],yearly[i][1]), (ind[i]+.2,y[i]) )
    plt.show()
    return years

def wincount(dframe,years,team):
    l=0
    w=0
    tie=0
    print('Team win-loss record by year:\n')
    for year in years:
        f,t = dframe.loc[year]['Europe_won'].value_counts(sort=False)
        print('{}: {}-{}'.format(year,f,t))
        if f>t:
            l+=1
        elif f<t:
            w+=1 
        else:
            tie+=1
    if 'a' in team:
        l,w = w,l
    print('\n')
    print( 'Total team win-loss-tie: {}-{}-{}\n'.format(w,l,tie)  )

def location(df,years,team):
    import pickle
    path = '//DREW/Users/andrew/Desktop/mosconi/'
    locs = pickle.load(open(path+'pkl/dloc','rb'))

    hm = []
    aw = []

    for year in years:
        if 'USA' in locs[year]:
            if 'a' in team.lower():
                hm.append(year)
            else:
                aw.append(year)
        else:
            if 'a' in team.lower():
                aw.append(year)
            else:
                hm.append(year)
    away = df.loc[aw]
    home = df.loc[hm]

    print( '\t Played home {} times, away {} times \n Home Games: {} \n Away Games: {}\n'.format(len(hm),len(aw),stats(home,team),stats(away,team)))
    return(home,away)

def location_split(home,away,team):
    hsing = stats(home[home['Format']=='Singles'],team)
    hdub = stats(home[home['Format']=='Doubles'],team)
    asing = stats(away[away['Format']=='Singles'],team)
    adub = stats(away[away['Format']=='Doubles'],team)

    print(' Home Singles: {} \n Home Doubles: {} \n Away Singles: {} \n Away Doubles: {}\n'.format(hsing,hdub,asing,adub))

def call_em(player,team):
    df,dframe = setup_df(player,team)
    sing,dub,teams,triples = overall_stats(df,team)
    print('-----Win-loss breakdown by partner----- \n')
    print(partners(dub,player))
    print('\n')
    print('-----Win-loss breakdown by opponent (singles)----- \n')
    print(opponents(sing))
    years = yearly_plot(df)
    wincount(dframe,years,team)
    home,away = location(df,years,team)
    location_split(home,away,team)
    return