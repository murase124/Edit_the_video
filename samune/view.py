import tkinter as tk
from controller import controller

class view:
    def __init__(self):
        self.controller = controller()

    #動画結合
    def movjoin(self):
        self.controller.movjoin([self.imgfileNameEntry.get(), self.movfileNameEntry.get()])

    #ファイル選択
    def dialogviewmov(self):
        print(self)
        filepath = self.controller.movdialogopen()#動画ファイル選択
        if len(filepath) == 0:#キャンセル
            return
        self.movfileNameEntry.delete(0, tk.END)
        self.movfileNameEntry.insert(tk.END, filepath)#ファイル名設定
    #ファイル選択
    def dialogviewimg(self):
        print(self)
        filepath = self.controller.imgdialogopen()#動画ファイル選択
        if len(filepath) == 0:#キャンセル
            return
        self.imgfileNameEntry.delete(0, tk.END)
        self.imgfileNameEntry.insert(tk.END, filepath)#ファイル名設定
    
    

    # メインウィンドウの生成
    def show(self):
        root = tk.Tk()
        root.title(u"動画編集")
        root.geometry("400x500")
        
        #ファイル名
        movfileNameLabelFrame = tk.LabelFrame(root, text=u'動画ファイル名', bd=2, relief=tk.GROOVE)
        movfileNameLabelFrame.pack(padx=5)
        self.movfileNameEntry = tk.Entry(movfileNameLabelFrame, width=30)
        self.movfileNameEntry.pack(padx=5, pady=5, side='left')
        dialog = tk.Button(movfileNameLabelFrame, text = "ファイル", width = 8,command=lambda : self.dialogviewmov())
        dialog.pack(padx=5, side='left')

        #ファイル名
        imgfileNameLabelFrame = tk.LabelFrame(root, text=u'画像ファイル名', bd=2, relief=tk.GROOVE)
        imgfileNameLabelFrame.pack(padx=5)
        self.imgfileNameEntry = tk.Entry(imgfileNameLabelFrame, width=30)
        self.imgfileNameEntry.pack(padx=5, pady=5, side='left')
        dialog = tk.Button(imgfileNameLabelFrame, text = "ファイル", width = 8,command=lambda : self.dialogviewimg()())
        dialog.pack(padx=5, side='left')

        #実行ボタン
        movencodeFrame = tk.LabelFrame(root, text='エンコード', bd=2, relief=tk.GROOVE)
        joinButton = tk.Button(movencodeFrame, text = "実行", width = 8)
        joinButton.bind("<Button-1>", lambda event: self.movjoin()) 
        joinButton.pack(padx=5, side='left')
        movencodeFrame.pack()

       

        root.mainloop()
