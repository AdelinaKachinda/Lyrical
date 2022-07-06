import os
import json
import requests
import lyricsgenius


def get_lyrics(artist, title):
  base_url = 'https://api.lyrics.ovh/v1/'
  url = base_url + artist + "/" + title 

  response = requests.get(url)
  print(response)

  lyrics = response.json()
  l_values = lyrics.values()

  for char in l_values:
    print(char)



# # genius api
# genius = lyricsgenius.Genius("pN39MdQbjguuvRXwSxcZ9FuPYb5zh-DzG_QT5qTME7NWwhZHRiLzeHDUUP8dK1_7")

# artist_name = input("Enter artist name: ").capitalize()
# max_songs = int(input(f"How many songs of {artist_name} do you want? "))


# artist = genius.search_artist(artist_name, max_songs, sort="title")
# print(artist.songs)
# print("\n")

# song_name = input("Which song title amongst these do you want the lyrics to? ")
# song = genius.search_song(song_name, artist.name)
# # artist.save_lyrics()

# print(song.lyrics)

def main():
  user_response = list(input("Enter name of an artist \" + \"song: " + "(e.g Burna Boy + ye)").strip().split("+"))
  artist_name = user_response[0].strip(" ")
  song_name = user_response[1].strip(" ")
  get_lyrics(artist_name, song_name)
  
  # print(user_response)




if __name__ == "__main__":
    main()








































































































