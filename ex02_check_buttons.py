from tkinter import IntVar

import ttkbootstrap as tb


class App:
    def __init__(self):
        self.root = tb.Window(themename='superhero')
        self.root.title('TTK Bootstrap')
        self.root.geometry('500x350')

        self.counter = 0

        self.my_label = tb.Label(text="Click the check button below.",
                                 font=('Helvetica', 28),
                                 style='info')
        self.my_label.pack(pady=(40, 10))

        self.var1 = self._check1()

        self._check2()
        self._check3()
        self._check4()
        self._check5()

    def _check5(self):
        self.var5 = IntVar()
        self.my_check5 = tb.Checkbutton(text="Square toggle",
                                        style='warning, square-toggle, outline',
                                        variable=self.var5,
                                        onvalue=1,
                                        offvalue=0,
                                        command=self.checker)
        self.my_check5.pack(pady=10)

    def _check4(self):
        self.var4 = IntVar()
        self.my_check4 = tb.Checkbutton(text="Round toggle",
                                        style='success, round-toggle, outline',
                                        variable=self.var4,
                                        onvalue=1,
                                        offvalue=0,
                                        command=self.checker)
        self.my_check4.pack(pady=10)

    def _check3(self):
        self.var3 = IntVar()
        self.my_check3 = tb.Checkbutton(text="Toolbutton",
                                        style='danger, toolbutton, outline',
                                        variable=self.var3,
                                        onvalue=1,
                                        offvalue=0,
                                        command=self.checker)
        self.my_check3.pack(pady=10)

    def _check2(self):
        self.var2 = IntVar()
        self.my_check2 = tb.Checkbutton(text="Toolbutton",
                                        style='danger, toolbutton',
                                        variable=self.var2,
                                        onvalue=1,
                                        offvalue=0,
                                        command=self.checker)
        self.my_check2.pack(pady=10)

    def _check1(self):
        var1 = IntVar()
        my_check = tb.Checkbutton(text="Check Me Out!",
                                  style='primary',
                                  variable=var1,
                                  onvalue=1,
                                  offvalue=0,
                                  command=self.checker)
        my_check.pack(pady=10)
        return var1

    def checker(self):
        if self.var1.get() == 1:
            self.my_label.config(text="You've checked the button.")
        else:
            self.my_label.config(text="Click the check button below.")

    def run(self):
        self.root.mainloop()


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
