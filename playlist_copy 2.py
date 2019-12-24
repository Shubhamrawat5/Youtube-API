from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# opening the file with dict containing title and videoID
r = open("playlist_title_videoId.txt", 'r', encoding='utf-8')
content = r.read()

# converting the string to dictionary with eval()
d = eval(content)
print(d)

# Displaying all the files details ---------------------->
print('<------ Displaying all the files details ------------>')
CO = 0
for title in d.keys():
    CO = CO+1
    titles = title
    v = d[title]
    print(CO, v, titles)

print('<---------------------------------------------------->')
print("Total videos are ",len(d))

CLIENT_SECRET_FILE = 'client.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials = flow.run_console()
# creating autorization code
youtube = build('youtube', 'v3', credentials=credentials)
print(youtube)
count = 0


def AddingVideosToPlaylist(title, videoID):
    print(videoID,title)
    global count
    count = count + 1
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

c = 0
for title in d.keys():
    c = c + 1
    if c < 141:
        pass
    else:
        AddingVideosToPlaylist(title, d[title])
