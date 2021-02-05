from moviepy.editor import *
from shutil import copyfile
import os

video_src_path = input("Enter the full path of the video: ")

if os.path.exists(video_src_path):
    try:
        f = open(video_src_path, 'r+')
        print("File found!")
        video_name = f.name.split("\\")[-1]
        video_dst_path = os.getcwd() + f"\\{video_name}"
        copyfile(src=video_src_path, dst=video_dst_path)
        audio_name = input("Enter the audio file name: ") + ".mp3"

        videoClip = VideoFileClip(filename=video_name)
        audioClip = videoClip.audio
        audioClip.write_audiofile(audio_name)
        audioClip.close()
        videoClip.close()

        os.remove(video_dst_path)

        audio_src_path = os.getcwd() + f"\\{audio_name}"
        audio_dst_path = video_src_path.replace(video_name, audio_name)
        copyfile(src=audio_src_path, dst=audio_dst_path)

        os.remove(audio_src_path)
        f.close()
    except OSError:
        print("File format not supported or something went wrong!")
        print(OSError)
    except NotImplementedError:
        print(NotImplementedError)
else:
    print("File does not exist at " + str(video_src_path))
