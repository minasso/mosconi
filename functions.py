def winlosslist(player, country, df):
    
    #singles
    if 'a' in country:
        swin=df[america_won&singles&d[player]].shape[0]
        sloss=df[d[player]&~america_won&singles].shape[0]
    else:
        sloss=df[d[player]&america_won&singles].shape[0]
        swin=df[d[player]&~america_won&singles].shape[0]        
    swl='{}-{}'.format(swin,sloss)
    try:
        spct=swin*100/(swin+sloss)
    except:
        spct=0
    
    #doubles
    if 'a' in country:
        dwin=df[d[player]&america_won&doubles].shape[0]
        dloss=df[d[player]&~america_won&doubles].shape[0]
    else:
        dloss=df[d[player]&america_won&doubles].shape[0]
        dwin=df[d[player]&~america_won&doubles].shape[0] 
    dwl='{}-{}'.format(dwin,dloss)
    try:
        dpct=dwin*100/(dwin+dloss)   
    except:
        dpct=0
    
        #teams
    if 'a' in country:
        twin=df[d[player]&america_won&teams].shape[0]
        tloss=df[d[player]&~america_won&teams].shape[0]
    else:
        tloss=df[d[player]&america_won&teams].shape[0]
        twin=df[d[player]&~america_won&teams].shape[0] 
    twl='{}-{}'.format(twin,tloss)
    try:
        tpct=twin*100/(twin+tloss)   
    except:
        tpct=0
        
        #triples
    if 'a' in country:
        trwin=df[d[player]&america_won&triples].shape[0]
        trloss=df[d[player]&~america_won&triples].shape[0]
    else:
        trloss=df[d[player]&america_won&triples].shape[0]
        trwin=df[d[player]&~america_won&triples].shape[0] 
    trwl='{}-{}'.format(trwin,trloss)
    try:
        trpct=round(trwin*100/(trwin+trloss),2)        
    except:
        trpct=0

    #combined
    cwin=dwin+swin+twin+trwin
    closs=dloss+sloss+tloss+trloss
    cwl='{}-{}'.format(cwin,closs)
    cpct=cwin*100/(cwin+closs)
    l=[player,country,swin,sloss,swl,round(spct,2),dwin,dloss,dwl,round(dpct,2), twl,trwl, cwin,closs,cwl,round(cpct,2)]
    return(l)
import pandas as pd
import pickle
df = pickle.load(open('allyears_with_teams','rb'))
winlosslist('Shane Van Boening','am',df)