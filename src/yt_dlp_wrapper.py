'''
Wrapper functions for yt-dlp
'''
from yt_dlp import YoutubeDL

# Downloads video using YoutubeDL
def download_video(url):
    with YoutubeDL() as ydl:
        ydl.download(url)
        