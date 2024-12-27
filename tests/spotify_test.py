import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from handler.spotify_handler import SpotifyHandler

spotify = SpotifyHandler()

def main():
    pass

# 1) ¿How long does it take for a raggaeton artist in Puerto Rico to become recognized in relation to Colombia and what factors influence this?

def question1():
    pr = "PR"
    co = "CO"
    pr_new_releases= spotify.get_country_new_releases(pr)
    co_new_releases= spotify.get_country_new_releases(co)
    delarose = "54seKvtsZauR1iauN0ptpo"
    deLaRosemusic=spotify.get_artist_music(delarose)
    delarose_data = spotify.get_artist(delarose)
    jayp="4NGOJedxkGWwkbB5QiSJd1"
    jayp_data=spotify.get_artist(jayp)
    jayp_music=spotify.get_artist_music(jayp)
    print(pr_new_releases)

def question2():
    reggaeton = spotify.search_artists_by_genre("reggaeton")
    juan_duque= "49ggXUsjVHl7BwwaiPUCn6"
    juan_duque_data=spotify.get_artist(juan_duque)
    pop = spotify.search_artists_by_genre("pop")
    ela_taubert= "5xS8cfsAaFyy188dNJGDbM"
    ela_taubert_data=spotify.get_artist(ela_taubert)
    vallenato = spotify.search_artists_by_genre("vallenato")
    elder_dayan= "0w8jfjckFjwtKLRkX9NT2K"
    elder_dayan_data=spotify.get_artist(elder_dayan)
    popular = spotify.search_artists_by_genre("popular")
    luis_alfonso= "0GchaVw5KfSVEm0xl0OXEe"
    luis_alfonso_data=spotify.get_artist(luis_alfonso)


# # 3)How does the impact of a collaboration (remix) between artists depending on musical genre and geographic region?

# -case 1 (Emergent artist: Heredero, Established artist:Jessi Uribe,Genere:Carranga,Countri:Colombia)
def question3():
    exitos_co="37i9dQZEVXbKrooeK9WSFF"
    song1="5enCBu8FLjlLz60k9t15MA"
    song1_remix="6rq3raDazN9D0XUCudW1Nx"
    song1_data=spotify.get_song(song1)
    song1_remix_data=spotify.get_song(song1_remix)
    heredero="6lH7FsK8dwGhPaz6mE2PgY"
    heredero_data=spotify.get_artist(heredero)
    jessi="3SN7I8KV2qBwTCZ4aNDcbS"
    jessi_data=spotify.get_artist(jessi)
# -case 2 (Emergent artist:Mora , Established artist:Bad bunny-Sehc,Genere:Reggaeton,Country:Puerto Rico)
    song2="4M6xyu1AHnaWAN8lHMNeo0"
    song2_remix="0G2zPzWqVjR68iNPmx2TBe"
    song2_data=spotify.get_song(song2)
    song2_remix_data=spotify.get_song(song2_remix)
    mora="0Q8NcsJwoCbZOHHW63su5S"
    mora_data=spotify.get_artist(mora)
    bad_bunny="4q3ewBCX7sLwd24euuV69X"
    bad_bunny_data=spotify.get_artist(bad_bunny)
    sech="77ziqFxp5gaInVrF2lj4ht"
    sech_data=spotify.get_artist(sech)
# -case 3 (Emergent artist:The weekend , Established artist:Ariana Grande,Genere:Pop,Country:USA)
    song3="5QO79kh1waicV47BqGRL3g"
    song3_remix="37BZB0z9T8Xu7U3e65qxFy"
    song3_data=spotify.get_song(song3)
    song3_remix_data=spotify.get_song(song3_remix)
    the_weekend="1Xyo4u8uXC1ZmMpatF05PJ"
    the_weekend_data=spotify.get_artist(the_weekend)
    ariana_grande="66CXWjxzNUsdJxJ2JdwvnR"
    ariana_grande_data=spotify.get_artist(ariana_grande)


# 4) How does an artist's release frequency affect their long-term popularity?
def question4():
    bad_bunny = "4q3ewBCX7sLwd24euuV69X"
    bad_bunny_data= spotify.get_artist(bad_bunny)
    bad_bunny_music = spotify.get_artist_music(bad_bunny)
    peso_pluma = "12GqGscKJx3aE4t07u7eVZ"
    peso_pluma_data= spotify.get_artist(peso_pluma)
    peso_pluma_music = spotify.get_artist_music(peso_pluma)
    feid = "2LRoIwlKmHjgvigdNGBHNo"
    feid_data= spotify.get_artist(feid)
    feid_music = spotify.get_artist_music(feid)
    karolG = "790FomKkXshlbRYZFtlgla"
    karolG_data= spotify.get_artist(karolG)
    karolG_music = spotify.get_artist_music(karolG)
    juniorH = "7Gi6gjaWy3DxyilpF1a8Is"
    juniorH_data= spotify.get_artist(juniorH)
    juniorH_music = spotify.get_artist_music(juniorH)
    top2024= "1VYdKkwhvk03yVitlPok09"
    top2024_data = spotify.get_playlist(top2024)

if __name__ == "__main__":
    question1()


