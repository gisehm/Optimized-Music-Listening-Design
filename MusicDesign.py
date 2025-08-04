import pandas as pd

df = pd.read_csv('SpotifyMostStreamedSongs.csv', engine = 'python')

#------------------------------------------------------------------
#method that outputs high danceability songs
def highdanceability(songchoice):
    return songchoice[songchoice.danceability >= df.danceability.mean()]

#method that outputs low danceability songs
def lowdanceability(songchoice):
    return songchoice[songchoice.danceability < df.danceability.mean()]

#------------------------------------------------------------------
#method that outputs high happiness (valence) songs
def highhappiness(songchoice):
    return songchoice[songchoice.valence >= df.valence.mean()]

#method that outputs low happiness (valence) songs
def lowhappiness(songchoice):
    return songchoice[songchoice.valence < df.valence.mean()]

#------------------------------------------------------------------
#method that outputs high energy songs
def highenergy(songchoice):
    return songchoice[songchoice.energy >= df.energy.mean()]

#method that outputs low energy songs
def lowenergy(songchoice):
    return songchoice[songchoice.energy < df.energy.mean()]

#------------------------------------------------------------------
#method that outputs high acousticness songs
def highacousticness(songchoice):
    return songchoice[songchoice.acousticness >= df.acousticness.mean()]

#method that outputs low acousticness songs
def lowacousticness(songchoice):
    return songchoice[songchoice.acousticness < df.acousticness.mean()]
            
#------------------------------------------------------------------
#method that outputs high liveness songs
def highliveness(songchoice):
    return songchoice[songchoice.liveness >= df.liveness.mean()]

#method that outputs low liveness songs
def lowliveness(songchoice):
    return songchoice[songchoice.liveness < df.liveness.mean()]
            
#------------------------------------------------------------------
#method that outputs high speechiness songs
def highspeechiness(songchoice):
    return songchoice[songchoice.speechiness >= df.speechiness.mean()]

#method that outputs low speechiness songs
def lowspeechiness(songchoice):
    return songchoice[songchoice.speechiness < df.speechiness.mean()]
            
#------------------------------------------------------------------

typemap = {"high danceability": highdanceability, "low danceability": lowdanceability, "high happiness": highhappiness, "low happiness": lowhappiness, "high energy": highenergy, "low energy": lowenergy, "high acousticness": highacousticness, "low acousticness": lowacousticness, "high liveness": highliveness, "low liveness": lowliveness, "high speechiness": highspeechiness, "low speechiness": lowspeechiness}

def cleanup(finalsongs):
    for i in finalsongs.itertuples():
        print(i.artist_names + " - " + i.track_name)

def tracklist(types):
    if ("high danceability" in types and "low danceability" in types) or ("high happiness" in types and "low happiness" in types) or ("high energy" in types and "low energy" in types) or ("high acousticness" in types and "low acousticness" in types) or ("high liveness" in types and "low liveness" in types) or ("high speechiness" in types and "low speechiness" in types):
        return cleanup(df)
    
    songs = df

    for x in types:
        choices = typemap.get(x)
        if choices:
            songs = choices(songs)

    return cleanup(songs)


print("What type of music are you looking for? (comma-separated): ")
inputs = [i.strip() for i in input().split(",")]

[x.lower() for x in inputs]
tracklist(inputs)
