from googleapiclient.discovery import build

api_key = 'AIzaSyDx_7S-_VSQGcp013Kcx0wxDJkzI1QbNZ4'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
        part='statistics',
        forUsername='fenerbahce'
    )

response = request.execute()

print(response)