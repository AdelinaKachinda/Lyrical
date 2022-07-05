import requests
import pprint
import json


artist = input("Enter the name of the artist: ")
title = input("Enter the title of the song: ")

base_url = 'https://api.lyrics.ovh/v1/'
url = base_url + artist + "/" + title 

response = requests.get(url)
print(response)

lyrics = response.json()
l_values = lyrics.values()

for line in l_values:
  print(line)


