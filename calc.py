import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self, w, h):
        super().__init__()
        self.geometry(f'{w}x{h}+{(self.winfo_screenwidth() - w) // 2}'
                      f'+{(self.winfo_screenheight() - h) // 2}')
        self.sc_f_frame = tk.Frame(self, padx=10, pady=10)
        self.sc_s_frame = tk.Frame(self, padx=10, pady=10)
        self.f_frame = tk.Frame(self, padx=10, pady=10)
        self.th_frame = tk.Frame(self, padx=10, pady=10)


class Btn(tk.Button):
    def __init__(self, parent, lbl, ent1, ent2, txt, side):
        super().__init__(parent)
        self.parent = parent
        self.ent1 = ent1
        self.ent2 = ent2
        self.txt = txt
        self.lbl = lbl
        self.side = side
        self.initUI()

    def initUI(self):
        self.btn = tk.Button(self.side,
                             text=self.txt,
                             command=self.swap)
        self.btn.pack(side='left', padx=10)

    def swap(self):
        params = self.ent1.give(), self.ent2.give()
        try:
            params = tuple(map(float, params))
            params = tuple(map(str, params))
            ans = eval(params[0] + self.txt + params[1])
            if float(int(float(ans))) == float(ans):
                self.lbl.swap(str(int(ans)))
            else:
                self.lbl.swap(ans)
            self.ent1.swap()
            self.ent2.swap()

        except ZeroDivisionError:
            self.lbl.swap('На ноль не дели')
            self.ent1.swap()
            self.ent2.swap()

        except ValueError:
            self.lbl.swap('Неверные вводные данные')
            self.ent1.swap()
            self.ent2.swap()


class Lable(tk.Label):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.lbl = tk.Label(self.parent.th_frame)
        self.lbl['text'] = 'Result here'
        self.lbl.pack(pady=10)

    def swap(self, txt):
        self.lbl['text'] = txt


class Entre(tk.Entry):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.entr = tk.Entry(self.parent.f_frame, width=20)
        self.entr.pack(pady=5, padx=5, side='left')

    def swap(self):
        self.entr.delete(0, 'end')

    def give(self):
        return self.entr.get()


if __name__ == '__main__':
    app = MainWindow(300, 200)
    enrty_f = Entre(app)
    enrty_s = Entre(app)
    lbl = Lable(app)
    btn1 = Btn(app, lbl, enrty_f, enrty_s, '+', app.sc_f_frame)
    btn2 = Btn(app, lbl, enrty_f, enrty_s, '-', app.sc_f_frame)
    btn3 = Btn(app, lbl, enrty_f, enrty_s, '*', app.sc_s_frame)
    btn4 = Btn(app, lbl, enrty_f, enrty_s, '/', app.sc_s_frame)
    app.f_frame.pack()
    app.sc_f_frame.pack()
    app.sc_s_frame.pack()
    app.th_frame.pack()
    app.mainloop()
