#!/usr/bin/python
from __future__ import print_function

import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
import time
import datetime
import breakline_function

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive'
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
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

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
    today= open('/Users/davisbooth/Desktop/Gilman_News_App/newsapp_sheet/today.txt', 'r')
    announcements= today.read().splitlines()
    today.close()
    values=[]
    cycle_day=["No School"]
    lunch=["No School"]
    sports=""
    other=""
    test_for_repeats=[]
    file= open("/Users/davisbooth/Desktop/Gilman_News_App/newsapp_sheet/sports_games.txt", "w")
    for announcement in announcements:
        if "DAY" in announcement:
            cycle_day=[announcement]
        elif "Varsity" in announcement or "F/S" in announcement or "JV" in announcement:
            sports+=breakline_function.breaklines(announcement, 32) + "\n\n"
            file.write(announcement+"\n")
        else:
            if announcement in test_for_repeats:
                pass
            else:
                test_for_repeats.append(announcement)
                other+=breakline_function.breaklines(announcement,32) + "\n\n"
    if sports=="":
        sports= "No games today"
        file.write(sports)
    if other=="":
        other="No other announcements"
    file.close()
    #----------------------------------------------Get Assembly---------------------------------------------------------------#
    assembly_sheet_id='1cJGqEOky2TvvNG0f8glYcC624Eyh9_NvKP9Td930tuM'
    cells='sheet1!A2:E'
    now = datetime.datetime.now()
    if now.hour>19:
        now= datetime.datetime.now() + datetime.timedelta(hours=24)
    current_month= now.strftime("%B")
    current_day= now.strftime("%d")
    if current_day[0]=='0':
        current_day=current_day[1]
    results= service.spreadsheets().values().get(spreadsheetId=assembly_sheet_id, range=cells).execute()
    all_assem = results.get('values', [])
    row_num=0
    todays_assembly=["No School"]
    for row in all_assem:
        if len(row)!=0:
            month=str(row[0])
            if month[0:2]== current_month[0:2]:
                assembly_month=month
                start_of_month=row_num
                break
        row_num+=1
    for num in range(start_of_month, len(all_assem)):
        day=all_assem[num]
        if len(day)!=0:
            if day[0]!=assembly_month:
                print("No assembly for today")
                break
            if day[1]==current_day:
                todays_assembly=[breakline_function.breaklines(day[4],33)]
                break
    #-----------------------------------------Clubs-----------------------------------------------------------------------#
    clubs=[]
    club_string=''
    club_range= "Sheet1!A:C"
    club_id='1vDuZNAkdPiiW_hSQALb98UVtagFUUP8d1xycfu8RfYA'
    clubs_data= service.spreadsheets().values().get(spreadsheetId=club_id, range=club_range).execute()
    clubs_data= clubs_data.get('values', [])
    cycle_day_today= str(cycle_day[0])
    if cycle_day_today == 'No School':
            clubs.append("No Clubs Today")
    else:
        cycle_day_today= cycle_day_today[4:]
        for row in clubs_data:
            if cycle_day_today == '1':
                if cycle_day_today in row[2] and '10' not in row[2]:
                    club_string+=breakline_function.breaklines(row[0],33) + '\n\n'
            else:
                if cycle_day_today in row[2]:
                    club_string+=breakline_function.breaklines(row[0],33) + '\n\n'
        clubs.append(club_string)
    #-----------------------------------------Get Lunch-----------------------------------------------------------------------#
    lunch_file=open('/Users/davisbooth/Desktop/Gilman_News_App/newsapp_sheet/todays_lunch.txt', 'r')
    items=lunch_file.readlines()
    lunch_file.close()
    lunch_today=""
    if len(items)!=0:
        for item in items:
            lunch_today+=item
        lunch=[lunch_today]
    #-------------------------------------------------------------------------------------------------------------------------#
    other=[other]
    sports=[sports]
    now= datetime.datetime.now()
    if now.hour>19:
        now= datetime.datetime.now()+ datetime.timedelta(hours=24)
    date= now.strftime("%A, %B %d, %Y")
    date=[breakline_function.breaklines(date, 32)]
    #------------------------------------------Stuff going up on excel---------------------------------------------------#
    spreadsheetId = '1ihLTmddFK2Mfr4VA894iMvMP_I01TGfKkLQGWl_X-AE'
    rangeName = '!A1'
    values.append(date)
    body= {'values': values}
    service.spreadsheets().values().update(spreadsheetId=spreadsheetId, range=rangeName,valueInputOption='RAW', body=body).execute()
    values=[]
    rangeName= '!A3:A'
    values.append(["Cycle Day"])
    values.append(cycle_day)
    values.append(["Today's Assembly"])
    values.append(todays_assembly)
    values.append(["Lunch"])
    values.append(lunch)
    values.append(["Sports Games"])
    values.append(sports)
    values.append(["Clubs"])
    values.append(clubs)
    values.append(["Other Announcements"])
    values.append(other)
    body= {'values': values}
    service.spreadsheets().values().update(spreadsheetId=spreadsheetId, range=rangeName,valueInputOption='RAW', body=body).execute()







if __name__ == '__main__':
    main()
