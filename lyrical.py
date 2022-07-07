import os
import json
import pprint
import pandas as pd
import sqlalchemy as db
import requests
import lyricsgenius

# lyical.ovh
def get_lyrics():
  artist = input("Enter artist name: ").capitalize()
  title = input("Enter song title: ").capitalize()

  base_url = 'https://api.lyrics.ovh/v1/'
  url = base_url + artist + "/" + title 

  response = requests.get(url)
  print(response)

  lyrics = response.json()
  l_values = lyrics.values()

  for char in l_values:
    print(char)


# genius api
genius = lyricsgenius.Genius("pN39MdQbjguuvRXwSxcZ9FuPYb5zh-DzG_QT5qTME7NWwhZHRiLzeHDUUP8dK1_7")

def get_extra_information():
  artist_name = input("Enter artist name: ").capitalize()
  max_songs = int(input(f"How many songs of {artist_name} do you want? "))


  artist = genius.search_artist(artist_name, max_songs, sort="popularity")
  artist_dict = artist.to_dict()
  songs_list = artist_dict['songs']
  data = {}

  for songs_dict in songs_list:
    
    data[songs_dict['title']] = [songs_dict["id"], songs_dict["album"]["name"], songs_dict["release_date"], songs_dict["song_art_image_thumbnail_url"], songs_dict["lyrics"]]

  #pprint.pprint(data)

  df = pd.DataFrame.from_dict(data, orient = 'index') 
  
  engine = db.create_engine('sqlite:///artist_info.db')
  df.to_sql(f"Artist_Information", con=engine, if_exists='replace', index=False)
  query_result = engine.execute("SELECT * FROM Artist_Information;").fetchall()
  print(pd.DataFrame(query_result))



















  # Each key (song name) becomes a row and each cloumn is an array of the song attribute
  # for i in songs_dict_first:
  #   pprint.pprint(i)
  #   print()


# songs_dict_first = songs_list[0]
# songs_dict_second = songs_list[1]
# print(songs_dict_second["lyrics"])


  #new_file = my_file['description_annotation']
  # songs = file['songs']
  # detail1 = file["description"]["plain"]
  # my_list = [file["followers_count"], file['id'], file['image_url'], file['name'], file['is_meme_verified']]
  #df = pd.DataFrame.from_dict(new_file)  
  # print(df)
  
  

get_extra_information()

  # pprint.pprint(file, width = 4)
  # print(artist.songs)
  # print("\n")

  # song_name = input("Which song title amongst these do you want the lyrics to? ")
  # song = genius.search_song(song_name, artist.name)
  # artist.to_json()


  # print(song.lyrics)


def create_database():
    pass




# def main():
#   print("\n")
#   print("Would you rather pick out a song from various songs or get lyrics for a specific song?")
#   user = input("Type various or specific: ").lower()
#   if user == "specific":
#     get_lyrics()     
#   elif user == "various":
#     get_extra_information()

  



# if __name__ == "__main__":
#     main()







