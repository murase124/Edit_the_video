#path ファイルの保存先
#text 保存するテキスト
#encode 保存エンコードタイプ
from moviepy.editor import *
from pathlib import PurePath

def save(path, text, encode=None, inmode="w"):#ファイルに書き込み
        with open(path, mode=inmode, encoding=encode) as file:
            file.write(text)

filedefoltpath = str(PurePath(__file__).parents[0])+ '\\mov\\bird.mp4'
print(filedefoltpath)
clip = VideoFileClip(filedefoltpath)
print(type(clip.audio))