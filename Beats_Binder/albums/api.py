import requests
def addSongEntry(id):
    name = "generic song name"
    duration=124
    preview = 

def addAlbumEntry(id):
    id = 447279465
    name = "WE MUST LOVE"
    
def addAlbumEntry(id):
    id = str(id)
    url = "https://deezerdevs-deezer.p.rapidapi.com/album/" + id
    headers = {
    	"X-RapidAPI-Key": "dc2e72cb1cmsh271df14842a824bp190aaajsnf4720429b177",
    	"X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers).json()
    name = response["title"]
    cover = response["cover_medium"]
    genre = response["genres"]["data"][0]["name"]
    nb_tracks = response["nb_tracks"]
    duration = response["duration"]
    release_date = response["release_date"]
    record_type = response["record_type"]
    
    print(name+cover+genre+str(nb_tracks)+str(duration)+release_date+record_type)

addEntry(68496491)