import tkinter as tk
from tkinter import ttk
from controller import controller

class view:
    def __init__(self):
        self.controller = controller()
    
    #表の一覧取得
    def alltimes(self):
        times = []
        for itemid in list(self.get_iids()):
            time = self.tree.item(itemid, 'values')
            times.append(time[1])
        return times

    #動画結合
    def movjoin(self):
        self.controller.movjoin(self.alltimes())

    #ファイル選択
    def dialogview(self):
        print(self)
        filepath = self.controller.dialogopen()#動画ファイル選択
        if len(filepath) == 0:#キャンセル
            return
        self.fileNameEntry.delete(0, tk.END)
        self.fileNameEntry.insert(tk.END, filepath)#ファイル名設定
    


    #レコードをすべてiidをすべて取得
    def get_iids(self, item=None):
        for child in self.tree.get_children(item):
            yield child
            yield from self.get_iids(child)
    # 表にレコードの追加
    def TreeviewInsert(self):
        self.tree.insert(parent='', index='end', values=(len(list(self.get_iids()))+1, self.fileNameEntry.get(), self.controller.getmovlen(self.fileNameEntry.get())))
    
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
                                + ",名前：" + record_values[1]
                                + ",時間：" + record_values[2]):
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

        #動画登録・表クリア 
        movaddclearFrame = tk.Frame(root, bd=2, relief=tk.GROOVE)
        movaddclearFrame.pack(padx=5)
        #動画登録ボタン
        newCutTimeBoxCreateButton = tk.Button(movaddclearFrame, text = "追加", width = 8)
        newCutTimeBoxCreateButton.pack(padx=5, side='left')
        newCutTimeBoxCreateButton.bind("<Button-1>", lambda event: self.TreeviewInsert()) 
        #動画登録ボタン
        treeclear = tk.Button(movaddclearFrame, text = "動画クリア", width = 8)
        treeclear.pack(padx=5, side='left')
        treeclear.bind("<Button-1>", lambda event: self.TreeviewClear()) 

        # 列の識別名を指定
        columnNames = {'id':'番号', 'name':'名前', 'time':'時間', 'del':'削除'}
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
        joinButton = tk.Button(movencodeFrame, text = "結合", width = 8)
        joinButton.bind("<Button-1>", lambda event: self.movjoin()) 
        joinButton.pack(padx=5, side='left')
        movencodeFrame.pack()

       

        root.mainloop()
