from pytube import YouTube
link = input('Enter the youtube url:\n')
yt = YouTube(link)
videos = yt.streams.all()
video = list(enumerate(videos))
for i in video:
    print(i)
print('Enter the desired option to download the format\n')
dn_option = int(input('Enter the option: '))
dn_video = videos[dn_option]
try:
    dn_video.download()
except:
    print('Download failed\n')
    quit()
print('Downloaded successfully....\n')