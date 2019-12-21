from googleapiclient.discovery import build

# google API key
key = 'AIzaSyBVGP0P8VUVPQdOsDoFP3B12Odvvk7l3Kc'

yt = build('youtube', 'v3', developerKey=key)
print(type(yt))

res = yt.commentThreads().list(part='snippet',videoId='yeqARWqjkps',maxResults=100, order='time', textFormat='plainText').execute()
print(res)