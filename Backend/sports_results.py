#!/usr/bin/python
from __future__ import print_function

import os
import breakline_function
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
import datetime

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
    spreadsheetId_1='1Eh7S_xOsYfcNAV_Lx2RHRFtVarOENDQ4e-_ExALTMZ4'
#-------------------Clearing out sports results-----------------------------------------------------------------------------------------#
    values=[[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""]]
    body={"values":values}
    rangeName="Sheet1!A:A"
    service.spreadsheets().values().update(spreadsheetId=spreadsheetId_1, range=rangeName,valueInputOption='RAW', body=body).execute()
    rangeName="Sheet1!B:B"
    service.spreadsheets().values().update(spreadsheetId=spreadsheetId_1, range=rangeName,valueInputOption='RAW', body=body).execute()
    rangeName="Sheet1!C:C"
    service.spreadsheets().values().update(spreadsheetId=spreadsheetId_1, range=rangeName,valueInputOption='RAW', body=body).execute()
    rangeName="Sheet1!D:D"
    service.spreadsheets().values().update(spreadsheetId=spreadsheetId_1, range=rangeName,valueInputOption='RAW', body=body).execute()
#-------------------Putting games into "sports results" sheet---------------------------------------------------------------------------#
    x=datetime.datetime.now()
    file=open("/Users/davisbooth/Desktop/Gilman_News_App/newsapp_sheet/sports_games.txt", "r")
    games= file.read().splitlines()
    file.close()
    values=[]
    for game in games:
        game="Awaiting Score\n" + breakline_function.breaklines(game, 33)
        game= [game]
        values.append(game)
    body={"values":values}
    if str(values)=="[['No games today']]":
        temp=[["No Recent Sports Results"]]
        body={"values":temp}
        rangeName="Sheet1!A1"
        service.spreadsheets().values().update(spreadsheetId=spreadsheetId_1, range=rangeName,valueInputOption='RAW', body=body).execute()
    else:
        headers=[["Sports Results"]]
        body={"values":headers}
        rangeName="Sheet1!A1"
        service.spreadsheets().values().update(spreadsheetId=spreadsheetId_1, range=rangeName,valueInputOption='RAW', body=body).execute()
        headers=[["W/L"]]
        body={"values":headers}
        rangeName="Sheet1!B1"
        service.spreadsheets().values().update(spreadsheetId=spreadsheetId_1, range=rangeName,valueInputOption='RAW', body=body).execute()
        headers=[["Hounds Score"]]
        body={"values":headers}
        rangeName="Sheet1!C1"
        service.spreadsheets().values().update(spreadsheetId=spreadsheetId_1, range=rangeName,valueInputOption='RAW', body=body).execute()
        headers=[["Away Score"]]
        body={"values":headers}
        rangeName="Sheet1!D1"
        service.spreadsheets().values().update(spreadsheetId=spreadsheetId_1, range=rangeName,valueInputOption='RAW', body=body).execute()
#---------------Header------------------------------------------------------------------------------#
        rangeName="Sheet1!A2:A"
        body={"values":values}
        service.spreadsheets().values().update(spreadsheetId=spreadsheetId_1, range=rangeName,valueInputOption='RAW', body=body).execute()



if __name__ == '__main__':
    main()
