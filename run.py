import os, re
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import openai
from dotenv import load_dotenv


# set the environment variable
dotenv_path = os.environ.get("PRIVATE_API_KEY_PATH")
load_dotenv(dotenv_path)
openai.api_key = os.environ.get('OPENAI_API_KEY')

# authenticate the client
credentials, project = google.auth.default(scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
youtube = build('youtube', 'v3', credentials=credentials)


# prompt user for the video URL
video_url = input("Enter the YouTube video URL: ")
# video_url = 'https://www.youtube.com/watch?v=QUYODQB_2wQ&lc=UgyiYJzk2XMGjuIjsSx4AaABAg.9mYftIxYoRS9mgn2hI2WRg'

# extract video ID from the URL
video_id = re.findall(r"v=([-\w]{11})", video_url)
if not video_id:
    print("Invalid video URL.")
    exit()
video_id = video_id[0]


# function to get comments from a video
def get_comments(video_url, video_id, next_page_token='', comments=[]):
    try:
        if video_id:
            video_id = video_id.strip()
            response = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                pageToken=next_page_token,
                textFormat='plainText'
            ).execute()
        else:
            response = youtube.commentThreads().list(
                part='snippet',
                videoUrl=video_url,
                pageToken=next_page_token,
                textFormat='plainText'
            ).execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)

            if item['snippet']['totalReplyCount'] > 0:
                reply_comments = get_comments(video_url, video_id, item['id'], [])
                comments += reply_comments

        if 'nextPageToken' in response:
            get_comments(video_url, video_id, response['nextPageToken'], comments)

        return comments

    except HttpError as error:
        print(f"An error occurred: {error}")
        return comments


# get comments from video
comments = get_comments(video_url, video_id)

# write comments to file
with open(f'{video_id}-comments.txt', 'w', encoding='utf-8') as file:
    for comment in comments:
        file.write(comment + '\n')



