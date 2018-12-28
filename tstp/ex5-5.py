LPSongs = ["Crawling", "Numb", "New Divide"]
SSongs = ["Kissed by a Rose", "Crazy", "System"]
PCSongs = ["In the Air Tonight", "Take me Home", "Land of Confusion"]

artists = {"Linkin Park":LPSongs, "Seal":SSongs, "Phil Collins":PCSongs}

#for artist in artists:
#   print(artists[artist])

for artist in artists:
    for song in artists[artist]:
        print(song)
