from pytube import YouTube
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

url = str(input('[+] Paste the link of the video: '))
cls()

yt = YouTube(url)

informations = print("///     Informations About Video     ///")
title = print("[+] Title: ",(yt.title))
duration = print("[+] Duration: ",(yt.length))
views = print("[+] Views: ",(yt.views))
time.sleep(3)
cls()

print("Downloading...")
video = yt.streams.filter(only_audio = True)[0]
download = video.download()
split_download = download.split(".mp4")[0]
split_download = split_download+".mp3"
os.rename(download,split_download)

print("[+] Sucessfully Downloaded !")
exit()