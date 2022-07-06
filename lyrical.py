import os
import json
import lyricsgenius

genius = lyricsgenius.Genius("pN39MdQbjguuvRXwSxcZ9FuPYb5zh-DzG_QT5qTME7NWwhZHRiLzeHDUUP8dK1_7")

artist_name = input("Enter artist name: ").capitalize()
max_songs = int(input(f"How many songs of {artist_name} do you want? "))


artist = genius.search_artist(artist_name, max_songs, sort="title")
print(artist.songs)
print("\n")

song_name = input("Which song title amongst these do you want the lyrics to? ")
song = genius.search_song(song_name, artist.name)
# artist.save_lyrics()

print(type(song.lyrics))







































































































# import requests
# import pprint
# import json


# artist = input("Enter the name of the artist: ")
# title = input("Enter the title of the song: ")

# base_url = 'https://api.lyrics.ovh/v1/'
# url = base_url + artist + "/" + title 

# response = requests.get(url)
# print(response)

# lyrics = response.json()
# l_values = lyrics.values()

# for char in l_values:
  # print(char)

