import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from processing import *


class MainWnd(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        master.title("번호 자동으로 매기기 + .wav로 전환")
        # master.geometry(0, 0)
        master.resizable(False, False)
        self.master = master

        ttk.Label(self, text="위치:").grid(column=0, row=0)
        self.path = tk.StringVar()
        self.path_entered = ttk.Entry(self, width=60, textvariable=self.path)
        self.path_entered.grid(column=1, row=0)

        self.pathfinder = ttk.Button(self, text="열기", command=self.pathfinding)
        self.pathfinder.grid(column=2, row=0)

        self.ok = ttk.Button(self, text="확인", command=self.process)
        self.ok.grid(column=0, row=1)
        self.cancel = ttk.Button(self, text="취소", command=self.close)
        self.cancel.grid(column=1, row=1)

        self.pack()

    def pathfinding(self):
        filename = filedialog.askdirectory()
        self.path.set(filename)

    def close(self):
        self.quit()

    def process(self):
        path = self.path.get()
        files = getFiles(path)

        os.mkdir(path + "\\result")

        for i in range(len(files)):
            mp3toWav(path + '\\' + files[i], path + "\\result\\" + str(i) + '.wav')
