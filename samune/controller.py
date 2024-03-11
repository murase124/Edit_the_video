import sys, os
sys.path.append(os.path.dirname(__file__)[:-7])
import tkinter.filedialog as filedialog
from movEdit import movEdit
from pathlib import PurePath



class controller:
    def __init__(self):
        self.filedefoltpath = str(PurePath(__file__).parents[1])+ '\\mov\\'
        self.movEdit = movEdit(self.filedefoltpath)


    #ファイルダイヤログ
    def movdialogopen(self):
        fTyp = [("","*")]
        iDir = os.path.abspath(self.filedefoltpath)
        print(iDir)
        filepathful = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
        filename = (os.path.basename(filepathful))
        self.movEdit.inputmov(filename)
        return filename
    
     #ファイルダイヤログ
    def imgdialogopen(self):
        fTyp = [("","*")]
        iDir = os.path.abspath(self.filedefoltpath)
        filepathful = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
        filename = (os.path.basename(filepathful))
        self.movEdit.inputimg(filename)
        return filename
    
    #動画結合
    def movjoin(self, filenames):
        self.movEdit.output(self.movEdit.join(filenames))

    #動画の長さ
    def getmovlen(self, filename):
        return self.movEdit.len(filename)  