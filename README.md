# YouTube Channel Search
---

This program uses YouTube's API to search a
YouTube channel for a string and returns a
list of videos related to that string. Then
it extracts their video ids from json data
and uses those ids to create a YouTube
video link, and download those videos using
[youtube-dl](https://github.com/ytdl-org/youtube-dl/).
