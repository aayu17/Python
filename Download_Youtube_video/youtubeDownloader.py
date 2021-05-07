import pytube
from pytube import YouTube
video_link=input("ENTER VIDEO LINK :")
yt=pytube.YouTube(video_link)
video=yt.streams.first()
#path where video will get saved
video.download("----------path-----------")
print("Downloaded...")
