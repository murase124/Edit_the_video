import datetime
import tkinter as tk
from tkinter import ttk
from 個人.movEdit.oneFile.controller import fun

class view:
    def __init__(self):
        self.controller = fun()
    
    def alltimes(self):
        times = []            
        for itemid in list(self.get_iids()):
            time = self.tree.item(itemid, 'values')
            times.append({"start":time[1],"end":time[2]})
        return times

    def movcut(self):
        img = self.imgfileNameEntry.get() if self.imgfileNameEntry.get() != "" else None
        self.controller.movcut(self.fileNameEntry.get(), self.alltimes(), img)

    def movjoin(self):
        img = self.imgfileNameEntry.get() if self.imgfileNameEntry.get() != "" else None
        self.controller.movjoin(self.fileNameEntry.get(), self.alltimes(), img)

    #画像ファイル選択
    def dialogviewimg(self):
        print(self)
        filepath = self.controller.imgdialogopen()#動画ファイル選択
        if len(filepath) == 0:#キャンセル
            return
        self.imgfileNameEntry.delete(0, tk.END)
        self.imgfileNameEntry.insert(tk.END, filepath)#ファイル名設定

    #ファイル選択
    def dialogview(self):
        print(self)
        filepath = self.controller.dialogopen()#動画ファイル選択
        if len(filepath) == 0:#キャンセル
            return
        self.fileNameEntry.delete(0, tk.END)
        self.fileNameEntry.insert(tk.END, filepath)#ファイル名設定
        self.startTimeEntry.delete(0, tk.END)
        self.startTimeEntry.insert(tk.END,"00:00:00.000")#スタート時間リセット
        self.endtTimeEntry.delete(0, tk.END)
        endtime = datetime.datetime.strptime("00:00:00", '%H:%M:%S')
        endtime = endtime + datetime.timedelta(seconds=self.controller.getmovlen(self.fileNameEntry.get()))
        self.endtTimeEntry.insert(tk.END, endtime.strftime("%H:%M:%S.%f")[:-3])#エンド時間に動画時間を設定
        self.TreeviewClear()

    #レコードをすべてiidをすべて取得
    def get_iids(self, item=None):
        for child in self.tree.get_children(item):
            yield child
            yield from self.get_iids(child)
    # 表にレコードの追加
    def TreeviewInsert(self):
        s_format = '%H:%M:%S.%f'
        start = datetime.datetime.strptime(self.startTimeEntry.get(), s_format)
        end = datetime.datetime.strptime(self.endtTimeEntry.get(), s_format)
        dif = end - start
        self.tree.insert(parent='', index='end', values=(len(list(self.get_iids()))+1, start.strftime("%H:%M:%S.%f")[:-3], end.strftime("%H:%M:%S.%f")[:-3],  str(dif)[:-3]))
    # 表をクリア
    def TreeviewClear(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
    #表を選択,削除
    def selectrecord(self, event):
        # 選択行の判別
        record_id = self.tree.focus()
        # 選択行のレコードを取得
        record_values = self.tree.item(record_id, 'values')
        if tk.messagebox.askyesno(title="選択行の確認",
                                message="次の行を削除しますか=> "
                                + "番号： " + record_values[0]
                                + ",開始：" + record_values[1]
                                + ",終了：" + record_values[2]
                                + ",時間：" + record_values[3]):
            self.tree.delete(record_id)
            pass
        else:
            pass

    # メインウィンドウの生成
    def show(self):
        root = tk.Tk()
        root.title(u"動画編集")
        root.geometry("400x500")
        
        #ファイル名
        fileNameLabelFrame = tk.LabelFrame(root, text=u'ファイル名', bd=2, relief=tk.GROOVE)
        fileNameLabelFrame.pack(padx=5)
        self.fileNameEntry = tk.Entry(fileNameLabelFrame, width=30)
        self.fileNameEntry.pack(padx=5, pady=5, side='left')
        dialog = tk.Button(fileNameLabelFrame, text = "ファイル", width = 8,command=lambda : self.dialogview())
        dialog.pack(padx=5, side='left')
        #画像ファイル名
        imgfileNameLabelFrame = tk.LabelFrame(root, text=u'画像ファイル名', bd=2, relief=tk.GROOVE)
        imgfileNameLabelFrame.pack(padx=5)
        self.imgfileNameEntry = tk.Entry(imgfileNameLabelFrame, width=30)
        self.imgfileNameEntry.pack(padx=5, pady=5, side='left')
        dialog = tk.Button(imgfileNameLabelFrame, text = "ファイル", width = 8,command=lambda : self.dialogviewimg()())
        dialog.pack(padx=5, side='left')

        #切り取り時間入力
        cutLabelFrame = tk.LabelFrame(root, text='切り取り', bd=2, relief=tk.GROOVE)
        cutLabelFrame.pack(pady=7)
        startTimeFrame = tk.LabelFrame(cutLabelFrame, text='開始時間', bd=2, relief=tk.GROOVE)
        startTimeFrame.pack(padx=5, side='left')
        self.startTimeEntry = tk.Entry(startTimeFrame, width=20)
        self.startTimeEntry.insert(tk.END,"00:00:00.000")
        self.startTimeEntry.pack(padx=5, pady=5)
        endtTimeFrame = tk.LabelFrame(cutLabelFrame, text='終了時間', bd=2, relief=tk.GROOVE)
        endtTimeFrame.pack(padx=5, side='left')
        self.endtTimeEntry = tk.Entry(endtTimeFrame, width=20)
        self.endtTimeEntry.insert(tk.END,"00:00:00.000")
        self.endtTimeEntry.pack(padx=5, pady=5)
        #切り取り時間登録ボタン
        newCutTimeBoxCreateButton = tk.Button(cutLabelFrame, text = "追加", width = 8)
        newCutTimeBoxCreateButton.pack(padx=5, side='left')
        #表に追加ボタンの処理
        newCutTimeBoxCreateButton.bind("<Button-1>", lambda event: self.TreeviewInsert()) 

        # 列の識別名を指定
        columnNames = {'id':'番号', 'start':'開始', 'end':'終了', 'time':'時間'}
        # Treeviewの生成
        self.tree = ttk.Treeview(root, columns=list(columnNames.keys()), show='headings')
        self.tree.bind("<<TreeviewSelect>>", self.selectrecord)
        # 列の設定
        self.tree.column('#0',width=0, stretch='no')
        for name in columnNames.keys():
            self.tree.column(name, anchor='center', width=80)
        # 列の見出し設定
        self.tree.heading('#0',text='')
        for name, jpname in columnNames.items():
            self.tree.heading(name, text=jpname, anchor='center')
        # ウィジェットの配置
        self.tree.pack(pady=10)

        #実行ボタン
        movencodeFrame = tk.LabelFrame(root, text='エンコード', bd=2, relief=tk.GROOVE)
        cutButton = tk.Button(movencodeFrame, text = "分割", width = 8)
        cutButton.bind("<Button-1>", lambda event: self.movcut()) 
        cutButton.pack(padx=5, side='left')
        joinButton = tk.Button(movencodeFrame, text = "結合", width = 8)
        joinButton.bind("<Button-1>", lambda event: self.movjoin()) 
        joinButton.pack(padx=5, side='left')
        movencodeFrame.pack()

        root.mainloop()
