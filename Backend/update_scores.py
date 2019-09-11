#!/usr/bin/python
from __future__ import print_function

import os
import breakline_function
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.
        
        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.
        
        Returns:
        Credentials, the obtained credential.
        """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'sheets.googleapis.com-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.
        
        Creates a Sheets API service object and prints the names and majors of
        students in a sample spreadsheet:
        https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
        """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)
    file=open("/Users/davisbooth/Desktop/Gilman_News_App/newsapp_sheet/sports_games.txt", "r")
    games= file.read().splitlines()
    file.close()
    squarespace_sheet='1QJqxWuvrYZ8BFmJMwbJ-o_WAlCvUk7H_2qM7LQfvzRg'
    sportsresults_sheet='1Eh7S_xOsYfcNAV_Lx2RHRFtVarOENDQ4e-_ExALTMZ4'
    rangeName='Sheet1!A2:H'
    result = service.spreadsheets().values().get(spreadsheetId=squarespace_sheet, range=rangeName).execute()
    games_info = result.get('values', [])
    #-----------transferring data to "sports results" from "sports results from square space------------------------------------------------#
    row_to_delete=""
    for num in range(1,len(games_info)):
        row=games_info[num]
        if row!=[]:
            row_to_delete=num+2
            values=[]
            game_index=str(int(row[1])+1)
            score= row[4] + '\nGilman: '+ row[2] + ' Away: ' + row[3] + '\n\n'
            rangeName='Sheet1!A' + game_index
            result = service.spreadsheets().values().get(spreadsheetId=sportsresults_sheet, range=rangeName).execute()
            currently_in_cell= result.get('values', [])
            currently_in_cell=currently_in_cell[0][0]
            if "Awaiting Score\n" in currently_in_cell:
                print(currently_in_cell)
                currently_in_cell= currently_in_cell[currently_in_cell.index("Awaiting Score\n")+len("Awaiting Score\n"):]
                game_with_score= score+currently_in_cell
                values.append([game_with_score])
                body={"values":values}
                service.spreadsheets().values().update(spreadsheetId=sportsresults_sheet, range=rangeName,valueInputOption='RAW', body=body).execute()
    values=[]
    values=[['']]
    body={"values":values}
    letters=['A','B','C','D','E','F','G','H','I']
    if row_to_delete!="":
        for letter in letters:
            rangeName="Sheet1!"+ letter + str(row_to_delete)
            service.spreadsheets().values().update(spreadsheetId=squarespace_sheet, range=rangeName,valueInputOption='RAW', body=body).execute()

if __name__ == '__main__':
    main()
