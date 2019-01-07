import pandas as pd
from scrapingFunctions import extractUrls, extractData
import traceback

AVVIO = input('Start the process? y/n  ')

READ = input('Read the urls CSV? y/n  ')


if AVVIO.strip() == 'y':
    print('')
    links_leagues = ['https://www.transfermarkt.it/jumplist/startseite/wettbewerb/IT1',\
                    "https://www.transfermarkt.it/jumplist/startseite/wettbewerb/L1",\
                    "https://www.transfermarkt.it/jumplist/startseite/wettbewerb/FR1",\
                    "https://www.transfermarkt.it/jumplist/startseite/wettbewerb/ES1",\
                    "https://www.transfermarkt.it/jumplist/startseite/wettbewerb/GB1"]
    
    # step 1 - players url extraction
    
    print('Step 1')
    
    if READ == 'n':
        players_url = extractUrls(links_leagues)
        df_links_players = pd.DataFrame({'urls': players_url})
        df_links_players.to_csv('new_data/urls.csv', index=False)
        print('Step 1 OK - Extracted urls: '+str(len(players_url)))
    else: 
        df_links_players = pd.read_csv('new_data/urls.csv')
        print('Step 1 OK - Extracted urls: '+str(df_links_players.shape[0]))
    
    # step 2 - get the players' data 
    print('\nStep 2')
    mydata = pd.DataFrame()
    
    for i in range(len(df_links_players.urls)):
        df_help = extractData(df_links_players.urls[i], i)
        
        if isinstance(df_help, pd.DataFrame):
            mydata = pd.concat([mydata,df_help])
            mydata.reset_index(drop=True, inplace=True)   
    
    mydata.to_csv('new_data/mydata.csv', index=False)
    print('Step 2 OK - Extracted rows: '+str(mydata.shape[0])+'; Total players: '+str(len(list(set(mydata.name)))))
    
input('Press any button to terminate the application')