from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# json file downloaded from google credentials
CLIENT_SECRET_FILE = 'client.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials = flow.run_console()
# creating autorization code
youtube = build('youtube', 'v3', credentials=credentials)

print(youtube)

# function for comment on a video on youtube
def insert_comment(youtube, channel_id, video_id, text):
    insert_result = youtube.commentThreads().insert(
        part="snippet",
        body=dict(
            snippet=dict(
                channelId=channel_id,
                videoId=video_id,
                topLevelComment=dict(
                    snippet=dict(
                        textOriginal=text)
                )
            )
        )
    ).execute()

    comment = insert_result["snippet"]["topLevelComment"]
    author = comment["snippet"]["authorDisplayName"]
    text = comment["snippet"]["textDisplay"]
    print("Inserted comment for %s: %s" % (author, text))

# channel id & video id will be of that channel where we want to comment, not our channel id
insert_comment(youtube, 'UCkUq-s6z57uJFUFBvZIVTyg', 'jWh0FaRRZC4', "Testing from python")