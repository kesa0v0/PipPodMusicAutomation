import tkinter as tk
from mainwnd import MainWnd

from processing import *

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWnd(root)
    app.mainloop()
