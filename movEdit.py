from moviepy.editor import *
class movEdit:

    #path = "code/個人/動画編集/mov/"
    #self.defaltpath ファイルのデフォルトファイルへのパス
    #self.output_clip 出力する動画クリップ　配列
    #self.inputclip 読み込んだクリップ
    #読み込み
    def __init__(self, defaltpath):
        self.clipclear()
        self.defaltpath = defaltpath

    #読み込み
    def inputmov(self, movfilename):
        self.clip[movfilename] = VideoFileClip(self.defaltpath+movfilename)
        return movfilename
    
    def inputimg(self, movfilename):
        self.clip[movfilename] = ImageClip(self.defaltpath+movfilename).set_duration('00:00:01.50')
        return movfilename
    
    #リセット
    def clipclear(self):
        self.clip = {}
        self.cutnum = 0
    
    #特定クリップ削除
    def delclip(self, filename):
        del self.clip[filename]
    
    #書き出し
    def output(self, movfilenames):
        files = os.listdir(self.defaltpath)
        num = 0
        for clip in {key: val for key, val in self.clip.items() if key in movfilenames}.values():
            while True:
                num +=1
                if "output"+str(num)+".mov" not in files:
                    clip.write_videofile(self.defaltpath+"output"+str(num)+".mov",codec='libx264', audio_codec='aac',verbose=False, logger=None)
                    break
                elif num >= 1000:
                    break
    #結合
    def join(self, filenames):
        outclip = [self.clip[filename] for filename in filenames]
        self.clip["out"+str(self.cutnum+1)] = concatenate_videoclips(outclip)
        self.cutnum +=1
        return ["out"+str(self.cutnum)]


    #分割
    def cut(self, movfilename, times):
        outclipname = []
        for time in times:
            self.clip["out"+str(self.cutnum+1)] = self.clip[movfilename].subclip(time['start'], time['end'])
            outclipname.append("out"+str(self.cutnum+1))
            self.cutnum +=1
        return outclipname
    
    #動画時間
    def len(self, movfilename):
        return self.clip[movfilename].duration
    
    #clip渡す
    def getclip(self, movfilename):
        return self.clip[movfilename]
    
    #clip名前一覧渡す
    def getfilenames(self):
        return list(self.clip.keys())

    
