import os
from pydub import AudioSegment


def getFiles(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files


def mp3toWav(src, dst):
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    print("number:", dst)
    print("Source:", src)
    print()
