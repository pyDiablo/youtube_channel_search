"""

    Youtube Channel Search
    Written by: @pyDiablo

    This program uses YouTube's API to search a
    YouTube channel for a string and returns a
    list of videos related to that string. Then
    it extracts their video ids from json data
    and uses those ids to create a YouTube
    video link, and download those videos using
    youtube-dl.

"""

from googleapiclient.discovery import build
import os
import time

def connect_yt_api():
    api_key = os.environ['YT_API_KEY']
    
    youtube = build('youtube', 'v3', developerKey=api_key)

def search_yt_channel(yt_api_client):
    # Search a YouTube channel for videos with {search terms here} in title
    youtube = yt_api_client
    request = youtube.search().list(
        part='snippet',  # string, The *part* parameter specifies a comma-separated list of one or more search resource properties that the API response will include. Set the parameter value to snippet. (required)
        channelId='CHANNEL_ID_HERE',  # string, channel's id you want to search
        maxResults=25,  # integer, No. of results you want to be displayed
        order='viewCount',  # Allowed values: searchSortUnspecified, date, rating, viewCount, relevance, title, videoCount
        q='SEARCH_TERMS_HERE',  # string, Textual search terms to match
        )
    response = request.execute()
    return response


video_data = response['items']  # Extratcing video info from json data
video_ids = []  # List of video ids
video_urls = []  # List of video urls
# count = 0  count of urls currently downloading


# Extracting video ids from json data
for i in range(1, len(video_data)):
    video_ids.append(video_data[i]['id']['videoId'])

# Creating YouTube video links and adding them to a list
for id in video_ids:
    url = f'https://youtube.com/watch?v={id}'
    video_urls.append(url)

print(video_urls)
print()

# Dowload each video one by one using youtube-dl
# for url in video_urls:  Alternate way of doing the following
for i, url in enumerate(video_urls, 1):  # enumerate(iterable, start) adds an index 'i' to the iterable (e.g. lists) and returns a tuple
    # count = count + 1
    # print(f'Downloading {count} of {len(video_urls)}: {url}...')  Alternate way of doing the above
    print(f'Downloading {i} of {len(video_urls)}: {url}...')
    os.system(f'youtube-dl {url}')
    print('Pausing the execution for 5 mins')
    print()
    time.sleep(300)  # Wait for 5 mins (300 seconds)
