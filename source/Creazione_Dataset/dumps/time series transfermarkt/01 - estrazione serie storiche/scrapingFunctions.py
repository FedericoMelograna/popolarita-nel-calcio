import requests
from bs4 import BeautifulSoup
import ast
import numpy as np
import pandas as pd


def extractUrls(url_leagues):
    output = []
    headers = {"User-Agent":"Mozilla/5.0"}
    for url in url_leagues:
        index = BeautifulSoup(requests.get(url, headers=headers).text, 'lxml')
        div1 = index.find('div', attrs={'id': 'yw1'})
        table1 = div1.find('table')
        linksTeam = list(set(['https://www.transfermarkt.it'+x['href'] for x in table1.find_all('a', attrs={'class': 'vereinprofil_tooltip'})]))
        for link in linksTeam:
            page = BeautifulSoup(requests.get(link, headers=headers).text, 'lxml')
            table_i = page.find_all('table', attrs={'class': 'items'})[0]
            url_players = list(set(['https://www.transfermarkt.it'+x['href'] for x in table_i.find_all('a', attrs={'class':'spielprofil_tooltip'})]))
            output  += url_players
    return output

def extractData(url, i):
    headers = {"User-Agent":"Mozilla/5.0"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'lxml')
    errori_tot = 0
    i+=1
    # time series extraction
    try:
        soup2 = str(soup).split("jQuery(window).on('load',function()")[1].split("'data'")[1]
        soup2 = soup2[1:(soup2.find(']')+1)]
        lista = ast.literal_eval(soup2)
        df = pd.DataFrame(lista).drop(['marker','mw','x'], axis=1)
        
        # other useful values
        df['name'] = soup.title.text.split(' - ')[0]
        df['id1'] = url.split('/')[-1]
        df['id2'] = url.split('/')[-4]
        try:
            righeTab = soup.find("table", attrs = {"class": "auflistung"}).find_all("tr")    
            for r in righeTab:
                if "Posizione" in str(r):
                    df['role'] = r.find("td").text.strip()
                elif "Piede" in str(r):
                    df['foot'] = r.find("td").text.strip()
        except:
            df['foot'] = df['role'] = np.nan
        try:
            df['league'] = soup.find('span', attrs = {'class': 'mediumpunkt'}).text.strip()
        except: 
            df['league'] = np.nan
        try:
            df['nation'] = soup.find("span",attrs = {"itemprop":"nationality"}).text
        except:
            df['nation'] = np.nan
        try:
            df['age2'] = int(soup.find("span",attrs = {"itemprop":"birthDate"}).text.strip()[-3:-1])
        except:
            df['age2'] = np.nan
        try:
            df['height'] = float(soup.find("span",attrs = {"itemprop":"height"}).text[0:4].replace(",","."))
        except:
            df['height'] = np.nan
        
        print(str(i)+' - '+soup.title.text.split(' - ')[0]+' OK')
        
        return df
        
    except Exception as e:
        errori_tot += 1
        print(str(i)+' - '+soup.title.text.split(' - ')[0], end=' ')
        print(e)

