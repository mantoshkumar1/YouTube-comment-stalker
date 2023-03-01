## What does this Code Does?
When you run the program, it will prompt you to enter the URL of the YouTube video you 
want to fetch comments from. It will then fetch all the comments using the YouTube API 
and save them to a file in the format <video_id>_comments.txt.

Example: python main.py
Input: 'https://www.youtube.com/watch?v=QUYODQB_2wQ&lc=UgyiYJzk2XMGjuIjsSx4AaABAg.9mYftIxYoRS9mgn2hI2WRg'
Please note that application only accept long URLs.


## Development:
To create GOOGLE_APPLICATION_CREDENTIALS or explicitly create credential: please see https://cloud.google.com/docs/authentication/getting-started

To create a service account and generate a service account key file for your Google Cloud Platform project, follow these steps:

Go to the Google Cloud Console (https://console.cloud.google.com/)
Select your project from the dropdown in the top navigation bar.
Click on the "IAM & admin" option from the left-hand navigation menu.
Click on the "Service accounts" option.
Click on the "+ CREATE SERVICE ACCOUNT" button.
Enter a name and description for your service account.
Click on the "CREATE" button.
Grant the service account appropriate permissions to access the YouTube Data API.
Click on the "CREATE KEY" button.
Select the JSON key type and click on the "CREATE" button.
The key file will be downloaded to your local machine.
Once you have the service account key file, set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the file path of the key file in your Python script. You can then use the Google Cloud SDK to authenticate and access the YouTube Data API.

## Reference:
* YouTube Data API: https://developers.google.com/youtube/v3/docs/?apix=true