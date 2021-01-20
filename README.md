# YouTube Channel Search

This program uses YouTube's API to search a
YouTube channel for a string and returns a
list of videos containing that string. Then
it extracts their video ids from json data
and uses those ids to create a YouTube
video link, and download those videos using
[youtube-dl](https://github.com/ytdl-org/youtube-dl/).


## Instructions
You need to have the following for this to work:

* API Key for YouTube

	You can get it from [Google Developers Console](https://console.developers.google.com/)

* google-api-python-client

	Enter the following in terminal to install:

	  pip install google-api-python-client
