import requests
import json

API_KEY = "key"
CHANNEL_HANDLE = "MrBeast"


def get_playlist_id():

    try:

        url = "https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)

        data = response.json()

        channel_items = data['items'][0]

        channel_playlistId = channel_items['contentDetails']['relatedPlaylists']['uploads']

        return channel_playlistId
    
    except requests.exceptions.RequestException as e:
        raise e
    
if __name__ == "__main__":
    get_playlist_id()