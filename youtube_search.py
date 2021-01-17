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

API_KEY = os.environ['YT_API_KEY']
SERVICE = 'youtube'
SERVICE_VERSION = 'v3'


def connect_yt_api():
    youtube = build(SERVICE, SERVICE_VERSION, developerKey=API_KEY)
    return youtube


def search_yt_channel(yt_api_client):
    # Search a YouTube channel for videos with {search terms here} in title
    youtube = yt_api_client
    request = youtube.search().list(
        # string, The *part* parameter specifies a comma-separated list of one or more search resource properties that the API response will include. Set the parameter value to snippet. (required)
        part='snippet',
        channelId='CHANNEL_ID_HERE',  # string, channel's id you want to search
        maxResults=25,  # integer, No. of results you want to be displayed
        # Allowed values: searchSortUnspecified, date, rating, viewCount, relevance, title, videoCount
        order='viewCount',
        q='SEARCH_TERMS_HERE',  # string, Textual search terms to match
    )
    response = request.execute()
    return response


def extract_yt_video_id_from_data(yt_api_response):
    response = yt_api_response
    video_data = response['items']  # Extratcing video info from json data
    video_ids = []  # List of video ids
    # count = 0  count of urls currently downloading

    # Extracting video ids from json data
    for i in range(1, len(video_data)):
        video_ids.append(video_data[i]['id']['videoId'])

    return video_ids


def create_yt_links_from_ids(video_ids):
    # Creating YouTube video links and adding them to a list
    video_urls = []  # List of video urls
    for id in video_ids:
        url = f'https://youtube.com/watch?v={id}'
        video_urls.append(url)

    return video_urls


def download_yt_videos_from_list(video_urls):
    # Dowload each video one by one using youtube-dl
    # # for url in video_urls:  Alternate way of doing the following
    # enumerate(iterable, start) adds an index 'i' to the iterable (e.g. lists) and returns a tuple
    for i, url in enumerate(video_urls, 1):
        # count = count + 1
        # print(f'Downloading {count} of {len(video_urls)}: {url}...')  Alternate way of doing the above
        print(f'Downloading {i} of {len(video_urls)}: {url}...')
        os.system(f'youtube-dl {url}')
        print('Pausing the execution for 5 mins\n')
        time.sleep(300)  # Wait for 5 mins (300 seconds)


def main():
    client = connect_yt_api()
    api_response = search_yt_channel(client)
    ids = extract_yt_video_id_from_data(api_response)
    urls = create_yt_links_from_ids(ids)
    download_yt_videos_from_list(urls)
    print('Finished!')


if __name__ == '__main__':
    main()
