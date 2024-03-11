import sys, os
sys.path.append(os.path.dirname(__file__)[:-7])
import tkinter.filedialog as filedialog
from movEdit import movEdit
from pathlib import PurePath

class  fun:
    def __init__(self):
        self.filedefoltpath = str(PurePath(__file__).parents[1])+ '\\mov\\'
        print(self.filedefoltpath )
        self.movEdit = movEdit(self.filedefoltpath)


    #ファイルダイヤログ
    def dialogopen(self):
        fTyp = [("","*")]
        iDir = os.path.abspath(self.filedefoltpath)
        filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
        filepath =  os.path.basename(filepath)
        self.movEdit.inputmov(filepath)
        return filepath

     #画像ファイルダイヤログ
    def imgdialogopen(self):
        fTyp = [("","*")]
        iDir = os.path.abspath(self.filedefoltpath)
        filepathful = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
        filename = (os.path.basename(filepathful))
        self.movEdit.inputimg(filename)
        return filename
    #動画の長さ
    def getmovlen(self, filepath):
        return self.movEdit.len(filepath)  

    #動画分割
    def movcut(self, filepath, times, samune = None):
        self.movEdit.output(self.movEdit.cut(filepath, times))
        if samune != None:
            self.movEdit.output([samune])

    #動画結合
    def movjoin(self, filepath, times, samune = None):
        clip = self.movEdit.join(self.movEdit.cut(filepath, times))
        if samune != None:
            print([samune] + clip)
            clip = self.movEdit.join([samune] + clip)
        self.movEdit.output(clip)
    
    