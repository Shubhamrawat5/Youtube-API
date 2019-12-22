from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import time

# opening subs_list file
f = open("subs_list.txt", 'r', encoding='utf-8')
content = f.read()
print(content)
list = content.split(" ")
print(list)
print(list.index('Abb'))
print(list[450])
#twent to Abb [DONE]
# json file downloaded from google credentials
CLIENT_SECRET_FILE = 'client.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials = flow.run_console()
# creating autorization code
youtube = build('youtube', 'v3', credentials=credentials)
print(youtube)
count = 0

def subscribing(channel_name,channel_id):
    global count
    count = count + 1
    request = youtube.subscriptions().insert(
        part="snippet",
        body={
        "snippet": {
            "resourceId": {
                "kind": "youtube#channel",
                "channelId": channel_id
                }
            }
        }
    )
    response = request.execute()

    # print(response)
    print(str(count)+' '+channel_name+" Subscribe successfully")


print(len(list))
# 1700
for i in range(450,1700 , 2):
    time.sleep(0.5)
    subscribing(list[i], list[i+1])
