import requests

#API CONECTION 

url = "https://accounts.spotify.com/api/token"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

data = {
    "grant_type": "client_credentials",
    "client_id": "15c528e05d8947f8bcc3d60683421505",  
    "client_secret": "7af4880026714be3a83441c3dddbe556",  
}

response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    print(f"Token obtenido con éxito: {response.json()}")
else:
    print("Error:", response.status_code)
    print(response.text)  

auth = {
    "Authorization": "Bearer BQB5XeCfskMDQM1taA6P-ZlETJ-RsW1KokcNRIcM2ltyvoF2HiR0jO25nGgxifVzmqRwkefO6vdTkTKT_AT6lRhvr-VhTrSqzKsv-iOv2OBUSDxLOy8",
}

# ENDPOINTS SEARCH

# 1) ¿How long does it take for a raggaeton artist in Puerto Rico to become recognized in relation to Colombia and what factors influence this?
    

pr_new_releases = "https://api.spotify.com/v1/browse/new-releases?country=PR"
response3= requests.get(prtop50,headers=auth)
print(response3.json())

co_new_releases = "https://api.spotify.com/v1/browse/new-releases?country=CO"
response4= requests.get(cotop50,headers=auth)
print(response4.json())

deLaRose= "https://api.spotify.com/v1/artists/54seKvtsZauR1iauN0ptpo"
response4_1= requests.get(deLaRose,headers=auth)
print(response4_1.json())
deLaRosemusic= "https://api.spotify.com/v1/artists/54seKvtsZauR1iauN0ptpo/albums"
response4_2_2 = requests.get(deLaRosemusic,headers=auth)
print(response4_2_2.json())

jayp= "https://api.spotify.com/v1/artists/4NGOJedxkGWwkbB5QiSJd1"
response4_2= requests.get(jayp,headers=auth)
print(response4_2.json())
jayp_music= "https://api.spotify.com/v1/artists/4NGOJedxkGWwkbB5QiSJd1/albums"
response4_2_1 = requests.get(jayp_music,headers=auth)
print(response4_2_1.json())

does not work
thisIsDeLaRose = "https://api.spotify.com/v1/playlists/37i9dQZF1DZ06evO2qk1lH"
response4_1=requests.get(thisIsDeLaRose,headers=auth)
print(response4_1.json())

# 2)¿What is the average time it takes for a reggaeton artist in Colombia to reach 1 million monthly streams, compared to other musical genres??

url = "https://api.spotify.com/v1/search"

reggaeton 

params1 = {
    "q": "genre:reggaeton",
    "type": "artist",
    "market": "CO",
    "limit": 50
}
response21 = requests.get(url, headers=auth, params=params1)
print(response21.json())

juan_duque = "https://api.spotify.com/v1/artists/49ggXUsjVHl7BwwaiPUCn6"
response22 = requests.get(juan_duque, headers=auth)
print(response22.json())

pop/baladas

params2 = {
    "q": "genre:pop",
    "type": "artist",
    "market": "CO",
    "limit": 50
}
response22 = requests.get(url, headers=auth, params=params2)
print(response22.json())


ela_taubert = "https://api.spotify.com/v1/artists/5xS8cfsAaFyy188dNJGDbM"
response23 = requests.get(ela_taubert, headers=auth)
print(response23.json())

vallenato

params3 = {
    "q": "genre:vallenato",
    "type": "artist",
    "market": "CO",
    "limit": 50
}
response24 = requests.get(url, headers=auth, params=params3)
print(response24.json())

elder_dayan= "https://api.spotify.com/v1/artists/0w8jfjckFjwtKLRkX9NT2K"
response25 = requests.get(elder_dayan, headers=auth)
print(response25.json())

ranchera

params4 = {
    "q": "genre:popular",
    "type": "artist",
    "market": "CO",
    "limit": 50
}
response26 = requests.get(url, headers=auth, params=params4)
print(response26.json())

luis_alfonso= "https://api.spotify.com/v1/artists/0GchaVw5KfSVEm0xl0OXEe"
response27 = requests.get(luis_alfonso, headers=auth)
print(response27.json())

# 3)How does the impact of a collaboration (remix) between artists depending on musical genre and geographic region?

# -case 1 (Emergent artist: Heredero, Established artist:Jessi Uribe,Genere:Carranga,Countri:Colombia)

song1 "https://api.spotify.com/v1/tracks/5enCBu8FLjlLz60k9t15MA"
response6_"= requests.get(song1,headers=auth)
print(response6_2.json())

song1_remix= "https://api.spotify.com/v1/tracks/6rq3raDazN9D0XUCudW1Nx"
response6= requests.get(song1_remix,headers=auth)
print(response6.json())

heredero= "https://api.spotify.com/v1/artists/6lH7FsK8dwGhPaz6mE2PgY"
response7= requests.get(heredero,headers=auth)
print(response7.json())

jessi="https://api.spotify.com/v1/artists/3SN7I8KV2qBwTCZ4aNDcbS"
response8= requests.get(jessi,headers=auth)
print(response8.json())

exitos_co="https://api.spotify.com/v1/playlist/37i9dQZEVXbKrooeK9WSFF"
response9= requests.get(exitos_co,headers=auth)
print(response9.json())

# -case 2 (Emergent artist:Mora , Established artist:Bad bunny-Sehc,Genere:Reggaeton,Country:Puerto Rico)
song2= "https://api.spotify.com/v1/tracks/4M6xyu1AHnaWAN8lHMNeo0"
response10= requests.get(song2,headers=auth)
print(response10.json())
song2_remix= "https://api.spotify.com/v1/tracks/0G2zPzWqVjR68iNPmx2TBe"
response11= requests.get(song2_remix,headers=auth)
print(response11.json())

mora= "https://api.spotify.com/v1/artists/0Q8NcsJwoCbZOHHW63su5S"
response12= requests.get(mora,headers=auth)
print(response12.json())

bad_bunny= "https://api.spotify.com/v1/artists/4q3ewBCX7sLwd24euuV69X"
response13= requests.get(bad_bunny,headers=auth)
print(response13.json())

sech= "https://api.spotify.com/v1/artists/77ziqFxp5gaInVrF2lj4ht"
response14= requests.get(sech,headers=auth)
print(response14.json())

# -case 3 (Emergent artist:The weekend , Established artist:Ariana Grande,Genere:Pop,Country:USA)

song3= "https://api.spotify.com/v1/tracks/5QO79kh1waicV47BqGRL3g"
response15= requests.get(song3,headers=auth)
print(response10.json())
song3_remix= "https://api.spotify.com/v1/tracks/37BZB0z9T8Xu7U3e65qxFy"
response16= requests.get(song3_remix,headers=auth)
print(response11.json())

the_weekend= "https://api.spotify.com/v1/artists/1Xyo4u8uXC1ZmMpatF05PJ"
response13= requests.get(the_weekend,headers=auth)
print(response13.json())

ariana_grande= "https://api.spotify.com/v1/artists/66CXWjxzNUsdJxJ2JdwvnR"
response14= requests.get(ariana_grande,headers=auth)
print(response14.json())

# 4) How does an artist's release frequency affect their long-term popularity?

bad_bunny= "https://api.spotify.com/v1/artists/4q3ewBCX7sLwd24euuV69X"
response15= requests.get(bad_bunny,headers=auth)
print(response15.json())
bad_bunny_music= "https://api.spotify.com/v1/artists/4q3ewBCX7sLwd24euuV69X/albums"
response15_2 = requests.get(bad_bunny_music,headers=auth)
print(response15_2.json())

peso_pluma = "https://api.spotify.com/v1/artists/12GqGscKJx3aE4t07u7eVZ"
response16= requests.get(peso_pluma,headers=auth)
print(response16.json())
peso_pluma_music= "https://api.spotify.com/v1/artists/12GqGscKJx3aE4t07u7eVZ/albums"
response16_2 = requests.get(peso_pluma_music,headers=auth)
print(response16_2.json())

feid = "https://api.spotify.com/v1/artists/2LRoIwlKmHjgvigdNGBHNo"
response17 = requests.get(feid,headers=auth)
print(response17.json())

feid_music= "https://api.spotify.com/v1/artists/2LRoIwlKmHjgvigdNGBHNo/albums"
response17_2 = requests.get(feid,headers=auth)
print(response17_2.json())

karol_g = "https://api.spotify.com/v1/artists/790FomKkXshlbRYZFtlgla"
response18 = requests.get(karol_g,headers=auth)
print(response18.json())
karol_g_music= "https://api.spotify.com/v1/artists/790FomKkXshlbRYZFtlgla/albums"
response18_2 = requests.get(karol_g_music,headers=auth)
print(response18_2.json())

junior_h = "https://api.spotify.com/v1/artists/7Gi6gjaWy3DxyilpF1a8Is"
response19 = requests.get(junior_h,headers=auth)
print(response19.json())

junior_h_music= "https://api.spotify.com/v1/artists/7Gi6gjaWy3DxyilpF1a8Is/albums"
response19_2 = requests.get(junior_h_music,headers=auth)
print(response19_2.json())

top2024 = "https://api.spotify.com/v1/playlists/1VYdKkwhvk03yVitlPok09"
response20=requests.get(top2024,headers=auth)
print(response20.json())