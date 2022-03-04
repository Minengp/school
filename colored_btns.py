import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self, w, h):
        super().__init__()
        self.geometry(f'{w}x{h}+{(self.winfo_screenwidth() - w) // 2}'
                      f'+{(self.winfo_screenheight() - h) // 2}')
        self.btn_frame = tk.Frame(self, padx=10, pady=10)
        self.other_frame = tk.Frame(self, padx=10, pady=10)


class Btn(tk.Button):
    def __init__(self, parent, color, lbl, ent):
        super().__init__(parent)
        self.parent = parent
        self.color = color
        self.lbl = lbl
        self.ent = ent
        self.initUI()

    def initUI(self):
        self.btn = tk.Button(self.parent.btn_frame,
                             text=self.color[0],
                             command=self.swap)
        self.btn.pack(side='left', padx=10)

    def swap(self):
        self.ent.swap(self.color)
        self.lbl.swap(self.color)


class Lable(tk.Label):
    def __init__(self, parent, text):
        self.text = text
        self.parent = parent
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.lbl = tk.Label(self.parent.other_frame)
        self.lbl.config(text=self.text)
        self.lbl.pack(pady=10)
        return self.lbl

    def swap(self, color):
        self.lbl['bg'] = color


class Entre(tk.Entry):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.entr = tk.Entry(self.parent.other_frame, width=20)
        self.entr.pack(pady=10)

    def swap(self, color):
        self.entr.delete(0, 'end')
        self.entr.insert(0, color)


if __name__ == '__main__':
    app = MainWindow(300, 200)
    lbl = Lable(app, 'ганжа')
    ent = Entre(app)
    btn1 = Btn(app, 'red', lbl, ent)
    btn2 = Btn(app, 'blue', lbl, ent)
    btn3 = Btn(app, 'green', lbl, ent)
    btn4 = Btn(app, 'orange', lbl, ent)
    btn5 = Btn(app, 'purple', lbl, ent)
    app.other_frame.pack()
    app.btn_frame.pack()
    app.mainloop()
