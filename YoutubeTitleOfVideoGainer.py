# google-api-python-client

import googleapiclient.discovery


def get_songs_from_youtube_playlist(playlist_id, api_key):
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=api_key)

    songs = []

    try:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50  # You can adjust the number of results as needed
        )

        while request:
            response = request.execute()

            for item in response["items"]:
                snippet = item["snippet"]
                song = {
                    "title": snippet["title"],
                    "artist": snippet["videoOwnerChannelTitle"]
                }
                songs.append(song)

            request = youtube.playlistItems().list_next(request, response)

    except Exception as e:
        print(f"An error occurred: {e}")

    return songs


# Example usage of the function:
playlist_id = "YOUR_YOUTUBE_PLAYLIST_ID_HERE"
api_key = "YOUR_YOUTUBE_API_KEY_HERE"

songs = get_songs_from_youtube_playlist(playlist_id, api_key)

for song in songs:
    print(f"Title: {song['title']}, Artist: {song['artist']}")
