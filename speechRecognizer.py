import re
from dotenv import load_dotenv
import os
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi


load_dotenv()
url = "https://www.youtube.com/watch?v=I8DaJbSbenE"

API_KEY = os.getenv('YOUTUBE_API_KEY')


# Extracts Video ID which is needed for youtube API
VIDEO_ID = re.search(r'v=([a-zA-Z0-9_-]+)', url).group(1)


yt = YouTubeTranscriptApi.get_transcript(VIDEO_ID)

textOnly = "".join([l['text'] for l in yt])
pattern = r"([.,])"


res = re.sub(pattern, r"\1 ", textOnly)
print(res)
# # Create the YouTube Data API client
# youtube = build('youtube', 'v3', developerKey=API_KEY)

# # Call the captions().list method to retrieve the video's captions
# captions = youtube.captions().list(
#     part='snippet',
#     videoId=VIDEO_ID
# ).execute()

# # Extract the text of the captions
# print(captions)
# text = captions['items'][0]['snippet']['text']

# # Print the captions
# print(text)
