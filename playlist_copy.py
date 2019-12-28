# To get all the data (title and videoID) of our playlist

from googleapiclient.discovery import build

# google API key
key = 'AIzaSyBVGP0P8VUVPQdOsDoFP3B12Odvvk7l3Kc'

yt = build('youtube', 'v3', developerKey=key)
# dict for storing video title with its videoId
d = {}

# Function to get title and videoId of every video on playlist
def playlistItems(items, ResultOnPage):
    for i in range(ResultOnPage):
        try:
            title = items[i]['snippet']['title']
            # print(title,end="")
            videoId = items[i]['snippet']['resourceId']['videoId']
            # print(videoId)
            d[title] = videoId
        except:
            pass
    #print(d)
    #print(len(d))


result = yt.playlistItems().list(part='snippet', playlistId='PLoFpzuHUvnne28IGQp8Ph2DOhyNHaMAKe').execute()
print(result)

# Total Items
TotalItems = result['pageInfo']['totalResults']
print("Total video items are : ", TotalItems)

# results per page
ResultPerPage = result['pageInfo']['resultsPerPage']
print("Result per page are : ", ResultPerPage)

playlistItems(result['items'],ResultPerPage)

for totalItems in range(int(TotalItems/ResultPerPage)-1):
    NextPagetoken = result['nextPageToken']
    result = yt.playlistItems().list(part='snippet', playlistId='PLoFpzuHUvnne28IGQp8Ph2DOhyNHaMAKe',pageToken=NextPagetoken).execute()
    playlistItems(result['items'],ResultPerPage)

# For remaining vidoes
remaining = TotalItems-len(d)

if remaining != 0:
    NextPagetoken = result['nextPageToken']
    result = yt.playlistItems().list(part='snippet', playlistId='PLoFpzuHUvnne28IGQp8Ph2DOhyNHaMAKe',
                                     pageToken=NextPagetoken).execute()
    playlistItems(result['items'], remaining)

print(d)
print("Length of our formed dict is ",len(d))

# exporting the data to a text file
w = open("playlist_title_videoId.txt",'w', encoding='utf-8')
w.write(str(d))
w.close()