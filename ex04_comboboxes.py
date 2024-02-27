import ttkbootstrap as tb


class App:
    def __init__(self):
        self.root = tb.Window(themename='superhero')
        self.root.title('TTK Bootstrap')
        self.root.geometry('500x350')

        self.my_label = tb.Label(text="Hello World!",
                                 font=('Helvetica', 28),
                                 style='info')
        self.my_label.pack(pady=40)

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                'Saturday', 'Sunday']

        self.my_combo = tb.Combobox(values=days,
                                    style='success')
        self.my_combo.pack(pady=20)

        self.my_combo.current(0)

        self.my_button = tb.Button(text='Get Day',
                                   style='warning',
                                   command=self.get_day)
        self.my_button.pack(pady=20)

        self.my_label2 = tb.Label(text='Binding the combobox to a label',
                                  font=('Helvetica', 28),
                                  style='info')
        self.my_label2.pack(pady=20)

        self.my_combo2 = tb.Combobox(values=days,
                                     style='info')
        self.my_combo2.pack(pady=20)
        self.my_combo2.bind('<<ComboboxSelected>>', self.get_day2)

    def get_day(self):
        day = self.my_combo.get()
        self.my_label.config(text=day)

    def get_day2(self, _event):
        day = self.my_combo2.get()
        self.my_label2.config(text=day)

    def run(self):
        self.root.mainloop()


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
