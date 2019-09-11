#!/usr/bin/python
from __future__ import print_function

import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
import time 
import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


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
                                   'calendar-python-quickstart.json')

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
    """Shows basic usage of the Google Calendar API.
        
        Creates a Google Calendar API service object and outputs a list of the next
        10 events on the user's calendar.
        """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    
#    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    x= datetime.datetime.now()
    if x.hour>19:
        #This gets 12:05
        now_temp=datetime.datetime.now()+datetime.timedelta(hours=24-x.hour)- datetime.timedelta(minutes=x.minute-5)
        now= now_temp.isoformat()+ 'Z'
        today = datetime.datetime.today()
        #This gets 11:59
        tomorrow=  now_temp+datetime.timedelta(hours=24)- datetime.timedelta(minutes=10)
        print(tomorrow)
        tomorrow= tomorrow.isoformat() + 'Z'
    else:
        #This gets 12:01
        now=datetime.datetime.utcnow()- datetime.timedelta(hours=x.hour)- datetime.timedelta(minutes=x.minute-1)
        now= now.isoformat()+ 'Z'
        today = datetime.datetime.today()
        #This gets 11:59
        tomorrow=  today + datetime.timedelta(days=1) - datetime.timedelta(hours=x.hour)- datetime.timedelta(minutes=x.minute+1)
        tomorrow= tomorrow.isoformat() + 'Z'
    eventsResult = service.events().list(calendarId='primary', timeMin=now, timeMax=tomorrow, singleEvents=True).execute()
    events = eventsResult.get('items', [])

    page_token = None
    announcements=[]
    lunch=""
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:
            eventsResult = service.events().list(calendarId=calendar_list_entry['id'], timeMin=now, timeMax=tomorrow, singleEvents=True).execute()
            events = eventsResult.get('items', [])
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                if event['summary']=="Today's Menu":
                    lunch=event['description']
                else:
                    announcements.append(event['summary'])
                page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break
    file=open('/Users/davisbooth/Desktop/Gilman_News_App/newsapp_sheet/today.txt', 'w')
    lunch_file=open('/Users/davisbooth/Desktop/Gilman_News_App/newsapp_sheet/todays_lunch.txt', 'w')
    print("Today's announcements:\n")
    for a in announcements:
        print(a)
        file.write(a + "\n")
    if lunch!="":
        lunch_file.write(lunch)
    file.close()
    lunch_file.close()
    



if __name__ == '__main__':
    main()
