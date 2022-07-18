import pandas as pd
from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
from os import path
import pygsheets
from config import SPREADSHEET_ID, CREDS_PATH
    
def getTradeValues(superflex=True, include_picks=True):
    url = 'https://keeptradecut.com/dynasty-rankings?filters=QB|WR|RB|TE'
    if include_picks:
        url = url + '|RDP'
    if not superflex:
        url = url + '&format=1'
    players = BeautifulSoup(get(url).text, features='lxml').select('div[id=rankings-page-rankings] > div')
    player_list = []
    for player in players:
        e = player.select('div[class=player-name] > p > a')[0]
        pid = e.get('href').split('/')[-1]
        name = e.text.strip()
        try:
            team = player.select('div[class=player-name] > p > span[class=player-team]')[0].text.strip()
        except:
            team = None
        position = player.select('p[class=position]')[0].text.strip()[:2]
        position = 'PICK' if position == 'PI' else position
        try:
            age = player.select('div[class=position-team] > p')[1].text.strip()[:2]
        except:
            age = None
        val = int(player.select('div[class=value]')[0].text.strip())
        val_colname = 'SF Value' if superflex else 'Non-SF Value'
        player_list.append({'PlayerID':pid,'Name':name,'Team':team,'Position':position,'Age':age,val_colname:val})
    return pd.DataFrame(player_list)

def write_to_gsheet(service_file_path, spreadsheet_id, sheet_name, data_df):
    """
    this function takes data_df and writes it under spreadsheet_id
    and sheet_name using your credentials under service_file_path
    """
    gc = pygsheets.authorize(service_file=service_file_path)
    sh = gc.open_by_key(spreadsheet_id)
    try:
        sh.add_worksheet(sheet_name)
    except:
        pass
    wks_write = sh.worksheet_by_title(sheet_name)
    wks_write.clear('A1',None,'*')
    wks_write.set_dataframe(data_df, (1,1), encoding='utf-8', fit=True)
    wks_write.frozen_rows = 1

if __name__ == "__main__":
    df = getTradeValues()
    #create sheet name based on date
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    SHEET_NAME = 'KTC-'+date

    write_to_gsheet(CREDS_PATH, SPREADSHEET_ID, SHEET_NAME, df)
