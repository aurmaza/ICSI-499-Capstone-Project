import re

import os
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi

captions = ""


def getYoutubeCaptions(url):
    API_KEY = os.getenv('YOUTUBE_API_KEY')

    # Extracts Video ID which is needed for youtube API
    VIDEO_ID = re.search(r'v=([a-zA-Z0-9_-]+)', url).group(1)

    # Retrieves transcript of given video ID
    yt = YouTubeTranscriptApi.get_transcript(VIDEO_ID)

    # joins all of the text into one string
    textOnly = "".join([l['text'] for l in yt])

    # Addds correct spacing for the strings
    pattern = r"([.,])"

    res = re.sub(pattern, r"\1 ", textOnly)
    return res


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=0GHPWOEQbII&list=PLQJqw6PVkyiOf0XZ0jhHie8zduelvSq7N"
    captions = getYoutubeCaptions(url)
