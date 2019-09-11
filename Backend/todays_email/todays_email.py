import base64
import email
import datetime
import time
import html2text
from bs4 import BeautifulSoup
from apiclient import errors
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def intro():
    SCOPES= 'https://www.googleapis.com/auth/gmail.readonly'
    CLIENT_SECRET= 'client_secret.json'

    store= file.Storage('storage.json')
    creds= store.get()
    if creds is None or creds.invalid:
        flow= client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
        creds= tools.run_flow(flow, store)
    GMAIL= build('gmail', 'v1', http=creds.authorize(Http()))
    messages = GMAIL.users().messages().list(userId='me', q='from:calendar-notification@google.com').execute().get('messages', [])
    todays_email=""
    now= datetime.datetime.now()
    todays_date= now.strftime("%Y-%m-%d")
    for messageD in messages:
        message= GMAIL.users().messages().get(userId='me', id=messageD['id'], format='raw').execute()
        message_date= time.strftime('%Y-%m-%d', time.gmtime(int(message['internalDate'])/1000))
        if todays_date==message_date:
            print message['snippet']
            msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))
            mime_msg = email.message_from_string(msg_str)
            todays_email=mime_msg.as_string()
#            browser= webdriver.Chrome('/Users/claytonhebert/Downloads/chromedriver')
#            browser.get('https://www.googleapis.com/gmail/v1/users/gilmannewsdata@gmail.com/messages/'+ message['id'])
#            elm= browser.find_element_by_link_text('Today\'s Menu')
#            browser.implicitly_wait(10)
#            elm.click()
            break
    if todays_email!="":
        print("Success, found today's email")
    else:
        print("Error, no email found for today")
        sys.exit()
    print todays_email
    return todays_email


def format_email(todays_email):
    todays_email_file=open("todays_email.txt","w")
    announcements=False
    #This is splitting up announcements on to seperate lines
    if "All day" in todays_email:
        announcements=True
        start_of_email='gilmannewsdata@gmail.com, here is your schedule for'
        end_of_email='View your calendar at https://www.google.com/calendar/'
        todays_email=todays_email[todays_email.index(start_of_email):todays_email.index(end_of_email)]
        while "All day" in todays_email:
            todays_email_file.write(todays_email[0:todays_email.index("All day")]+"\n" + "All day")
            todays_email=todays_email[todays_email.index("All day")+ len("All day"):]
        todays_email_file.write(todays_email)
    #If there are no announcements
    if announcements==False:
        todays_email_file.write(todays_email)
    todays_email_file.close()
    return announcements

def data_from_email(announcements):
    daily_email=open("todays_email.txt", "r")
    email_data= daily_email.readlines()
    daily_email.close()
    today= open("today.txt","w")
    if announcements==False:
        today.write("No Announcments")
    for line in email_data:
        if "All Day" in line:
            data= line
            today.write(data+"\n")
    today.close()



def main():
    todays_email=intro()
    announcements=format_email(todays_email)
    data_from_email(announcements)

main()







