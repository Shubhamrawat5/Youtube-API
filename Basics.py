from googleapiclient.discovery import build

# google API key
key = 'AIzaSyBVGP0P8VUVPQdOsDoFP3B12Odvvk7l3Kc'

yt = build('youtube', 'v3', developerKey=key)
print(type(yt))

# id = channel id
res = yt.channels().list(id='UCzQdAOFO6_docu0f6Sn93wA', part='contentDetails').execute()

print(res)
# UPLOADS LIST #
result = yt.playlistItems().list(playlistId='UUzQdAOFO6_docu0f6Sn93wA', part='snippet', maxResults=50).execute()
print(result)
# print(len(result['items']))
# for i in range(len(result['items'])):
#    print(result['items'][i]['snippet']['title'])

# SUBSCRIPTIONS LIST #
res2 = yt.subscriptions().list(id='UCzQdAOFO6_docu0f6Sn93wA', part='subscriberSnippet').execute()
print(res2)
