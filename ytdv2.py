import pytube
import os

vid_url = input('Enter the youtube url: ').strip()
yt = pytube.YouTube(vid_url)
video = yt.streams.filter(only_audio=True).first()
dest = os.getcwd()
out_file = video.download(output_path=dest)
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
print('Successfully Downloaded.')