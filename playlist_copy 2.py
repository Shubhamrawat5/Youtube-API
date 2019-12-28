# Now copying in another youtube account
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# opening the file with dict containing title and videoID with 1st program
r = open("playlist_title_videoId.txt", 'r', encoding='utf-8')
content = r.read()

# converting the string to dictionary with eval()
d = eval(content)
print(d)

# Displaying all the files details ---------------------->
print('<------ Displaying all the files details ------------>')
COUNT = 0
for title in d.keys():
    COUNT = COUNT+1
    v_id = d[title]
    print(COUNT, v_id, title)

print('<---------------------------------------------------->')
print("Total videos are ", len(d))

# client.json file is downloaded from google api credentials OAuth 2.0
CLIENT_SECRET_FILE = 'client.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials = flow.run_console()

# creating autorization code
youtube = build('youtube', 'v3', credentials=credentials)
print(youtube)


# Function for adding the old playlist videos in our new playlist
# playlistId is our new playlist id
# videoID in argument is the yt video id of our old playlist video
def AddingVideosToPlaylist(title, videoID):
    print(videoID, title)
    request = youtube.playlistItems().insert(
        part="snippet",
            body={
            "snippet": {
                "playlistId": "PLnAugck5EkiIC8wuaRn0nAMUilK7og5Nf",
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": videoID
                    }
                }
            }
        )
    response = request.execute()
    print(count, title, 'added to playlist succesfully')


count = 0
#calling and iterating the video title & id of our old playlist videos
for title in d.keys():
    print(count, 'Video name: ', title)
    AddingVideosToPlaylist(title, d[title])
