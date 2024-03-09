

import pytube

url=input("Video Url'nizi giriniz: ")
path="C:\Eudor\Downloads"
pytube.YouTube(url).streams.get_audio_only().download(path)